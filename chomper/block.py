# Copyright: (c) 2018, Aniket Panjwani <aniket@addictedto.tech>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from typing import List, Dict, NamedTuple
import sys
import os
import shlex
import subprocess
import datetime
import json
import yaml
import click
from crontab import CronTab
sys.path.append('../')
import utils
from constants import TIME_FORMAT, MITMDUMP_COMMAND


@click.command()
@click.option('--rules_path', default='./data/rules.yaml',
              help='Path of rules file.')
@click.option('--settings_json_path', help='Path of time file.',
              default='../data/block_settings.json')
@click.option('--rule', default='coding')
@click.option('--listening_port', default=8080)
@click.option('--block_length', default=2,
              help='Time for which to maintain block in minutes.')
@click.option('--reset_command', type=str,
              help='Full path command to reset ports.',
              default='python reset.py')
@click.option('--mitmdump_bin_path', type=str,
              help='Full path command to mitmdump_binary.')
def main(rules_path: str, settings_json_path: str, rule: str,
         listening_port: int, block_length: int, reset_command: str,
         mitmdump_bin_path: str):

    # TODO: Check if user is root; else raise Exception.

    # Check if previous block's config file exists.
    new_block_start = datetime.datetime.now()
    new_block_end = new_block_start.replace(second=0) \
        + datetime.timedelta(minutes=block_length)
    if os.path.isfile(settings_json_path):
        with open(settings_json_path, 'r') as json_file:
            old_block_settings = json.load(json_file)
        # Old block is in effect.
        old_block_end = datetime.datetime.strptime(old_block_settings['end'],
                                                   TIME_FORMAT)
        if old_block_end > new_block_start:
            enact_block(old_block_settings['listening_port'],
                        old_block_settings['addresses'],
                        old_block_settings['block_type'],
                        mitmdump_bin_path, rule, old_block_settings['end'])
            set_block_length(old_block_end, reset_command)
            write_block_to_json(old_block_settings, settings_json_path)
            print("Did not enact new block."
                  " Old block still in effect until {}."
                  .format(old_block_settings['end']))
        # Old block has passed.
        else:
            new_block_settings \
                = create_block_dict(rules_path, listening_port, rule,
                                    new_block_start, new_block_end)
            enact_block(listening_port, new_block_settings['addresses'],
                        new_block_settings['block_type'],
                        mitmdump_bin_path, rule, new_block_settings['end'])
            set_block_length(new_block_end, reset_command)
            write_block_to_json(new_block_settings, settings_json_path)
            print("New block in effect until {}."
                  .format(new_block_settings['end']))
    # No previous config file.
    elif not os.path.isfile(settings_json_path):
        new_block_settings \
            = create_block_dict(rules_path, listening_port, rule,
                                new_block_start, new_block_end)
        enact_block(listening_port, new_block_settings['addresses'],
                    new_block_settings['block_type'],
                    mitmdump_bin_path, rule, new_block_settings['end'])
        set_block_length(new_block_end, reset_command)
        write_block_to_json(new_block_settings, settings_json_path)
        print("New block in effect until {}."
              .format(new_block_settings['end']))


def write_block_to_json(block_settings, json_path):
    with open(json_path, 'w') as f:
        json.dump(block_settings, f)


def set_block_length(block_end, reset_command):
    """Remove previous crontab rules and add new one."""
    cron = CronTab(user='root')
    cron.remove_all(comment='Chomper timer')
    job = cron.new(command=reset_command)
    job.month.on(block_end.month)
    job.day.on(block_end.day)
    job.hour.on(block_end.hour)
    job.minute.on(block_end.minute)
    job.set_comment('Chomper timer')
    cron.write()


def create_block_dict(rules_path, listening_port, rule, block_start, block_end):
    """Create a dictionary with block parameters which can be written to JSON."""

    with open(rules_path, 'r') as rules_file:
        yaml_import = yaml.load(rules_file.read())
    rules = {key: {'block_type': value[0]['block_type'][0],
                   'addresses': value[1]['addresses']}
             for key, value in yaml_import.items()}
    joined_urls = '$[]'.join(rules[rule]['addresses'])

    # Create block configuration JSON
    block_dict = {'start': block_start.strftime(TIME_FORMAT),
                  'end': block_end.strftime(TIME_FORMAT),
                  'listening_port': listening_port,
                  'block_type': rules[rule]['block_type'],
                  'addresses': joined_urls}
    return block_dict

def enact_block(listening_port: int, joined_addresses: str, block_type: str,
                mitmdump_bin_path: str, rule: str, block_end_time: str):
    """Function which enacts block."""

    # Flush any existing processes and reset networking.
    utils.reset_nat()
    try:
        utils.kill_process()
    # In case there are no mitmproxy processes open.
    except:
        pass

    # Set up TCP Routing
    utils.setup_nat(listening_port)

    # Start mitmdump, passing filter.py.
    args = shlex.split(MITMDUMP_COMMAND.format(mitmdump_bin_path,
                                               joined_addresses,
                                               block_type, rule,
                                               block_end_time))
    mitmdump = subprocess.Popen(args)

if __name__ == "__main__":
    main()
