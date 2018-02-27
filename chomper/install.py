# Copyright: (c) 2018, Aniket Panjwani <aniket@addictedto.tech>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


"""Detects operating system and guides installation."""

import platform
import distro
import time
import click
from utils import exec_command, kill_process

CERT_LOC = {'debian': '/usr/local/share/ca-certificates/mitmproxy-ca.crt',
            'antergos': '/etc/ca-certificates/trust-source/anchors/mitmproxy-ca.crt'}

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
    elif dist == 'antergos':
        install_antergos(user)
    else:
        print("Installation with your Linux distribution "
              "is currently not supported.")


def install_debian(user):
    exec_command('pipenv run screen -d -m mitmdump')
    time.sleep(2)
    kill_process()
    exec_command('openssl x509 -outform der -in ~/.mitmproxy/mitmproxy-ca.pem '
                 '-out ~/.mitmproxy/mitmproxy-ca.crt')
    exec_command('sudo cp /home/{}/.mitmproxy/mitmproxy-ca.crt {}'
                 .format(user, CERT_LOC['debian']))
    exec_command('sudo update-ca-certificates')
    exec_command('sudo sh ./chomper/certs.sh'.format(CERT_LOC['debian']))
    exec_command('sudo sysctl -w net.ipv4.ip_forward=1')
    exec_command('sudo sysctl -w net.ipv6.conf.all.forwarding=1')
    exec_command('sudo sysctl -p')
    print("Installation completed.")


def install_antergos(user):
    exec_command('pipenv run screen -d -m mitmdump')
    time.sleep(2)
    kill_process()
    exec_command('openssl x509 -outform der -in ~/.mitmproxy/mitmproxy-ca.pem '
                 '-out ~/.mitmproxy/mitmproxy-ca.crt')
    exec_command('sudo cp /home/{}/.mitmproxy/mitmproxy-ca.crt {}'
                 .format(user, CERT_LOC['arch']))
    exec_command('sudo trust extract-compat')
    exec_command('sudo sh ./chomper/certs.sh {}'.format(CERT_LOC['arch']))
    exec_command('sudo echo 1 > /proc/sys/net/ipv4/ip_forward')
    exec_command('sudo echo 1 > /proc/sys/net/ipv6/conf/all/forwarding')
    exec_command('sudo sysctl -p')
    print("Installation completed.")


def install_mac(user):
    print("MacOS is not currently supported.")


def install_windows(user):
    print("Windows is not supported.")

if __name__ == "__main__":
    main()
