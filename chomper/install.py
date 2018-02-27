# Copyright: (c) 2018, Aniket Panjwani <aniket@addictedto.tech>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


"""Detects operating system and guides installation."""

import os
import platform
import click


@click.command()
def main():
    _os = platform.system()
    if _os == 'Linux':
        install_linux()
    elif _os == 'Darwin':
        install_mac()
    elif _os == 'Windows':
        install_windows()

def install_linux():
    pass

def install_mac():
    print("MacOS is not currently supported.")

def install_windows():
    print("Windows is not supported.")

if __name__ == "__main__":
    main()
