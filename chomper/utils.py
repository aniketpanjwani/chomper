"""Utility functions to assist setting up port forwarding."""

import os
import subprocess
import shlex
import psutil


def exec_command(command):
    p = subprocess.Popen(shlex.split(command))
    p.wait()


def pause_sudo(username, sleep_time):
    exec_command('sh pause_sudo.sh {} {}'.format(username, sleep_time))


def reset_nat():
    exec_command('iptables -t nat -F')
    exec_command('ip6tables -t nat -F')


def setup_nat(listening_port):
    exec_command('iptables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner '
                 'root --dport 80 -j REDIRECT --to-port {0}'
                 .format(listening_port))
    exec_command('iptables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner '
                 'root --dport 443 -j REDIRECT --to-port {0}'
                 .format(listening_port))
    exec_command('ip6tables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner '
                 'root --dport 80 -j REDIRECT --to-port {0}'
                 .format(listening_port))
    exec_command('ip6tables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner '
                 'root --dport 443 -j REDIRECT --to-port {0}'
                 .format(listening_port))


def find_processes_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
        if name == p.info['name'] or \
                p.info['exe'] and os.path.basename(p.info['exe']) == name or \
                p.info['cmdline'] and p.info['cmdline'][0] == name:
            ls.append(p)
    return ls


def kill_process():
    processes = find_processes_by_name('mitmdump')
    for p in processes:
        p.kill()
