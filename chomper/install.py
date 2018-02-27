# Copyright: (c) 2018, Aniket Panjwani <aniket@addictedto.tech>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


"""Detects operating system and guides installation."""

import platform
import distro
import time
import click
from utils import exec_command, kill_process


@click.command()
@click.option('--user')
def main(user):
    _os = platform.system()
    if _os == 'Linux':
        install_linux(user)
    elif _os == 'Darwin':
        install_mac(user)
    elif _os == 'Windows':
        install_windows(user)


def install_linux(user):
    dist = distro.id()
    if dist in {'ubuntu', 'debian', 'linuxmint'}:
        install_debian(user)
    elif dist == 'arch':
        install_arch(user)
    else:
        print("Installation with your Linux distribution "
              "is currently not supported.")


def install_debian(user):
    exec_command('pipenv run screen -d -m mitmdump')
    time.sleep(2)
    kill_process()
    exec_command('openssl x509 -outform der -in ~/.mitmproxy/mitmproxy-ca.pem -out ~/.mitmproxy/mitmproxy-ca.crt')
    exec_command('sudo cp /home/{}/.mitmproxy/mitmproxy-ca.crt /usr/local/share/ca-certificates/mitmproxy-ca.crt'.format(user))
    exec_command('sudo update-ca-certificates')
    exec_command('sudo sh ./chomper/certs.sh')
    exec_command('sudo sysctl -w net.ipv4.ip_forward=1')
    exec_command('sudo sysctl -w net.ipv6.conf.all.forwarding=1')
    exec_command('sudo sysctl -p')


def install_arch(user):
    pass


def install_mac(user):
    print("MacOS is not currently supported.")


def install_windows(user):
    print("Windows is not supported.")

if __name__ == "__main__":
    main()
