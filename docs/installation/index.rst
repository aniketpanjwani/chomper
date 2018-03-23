Installation
============

Chomper can be installed on any Linux distribution. However, the installation has only been fully automated for Debian-based distributions. Automated installation scripts can be found in the `Chomper Installers repo <https://github.com/aniketpanjwani/chomper_installers>`__.

For each installation method, you will need to be using a user with sudo privileges.

############
Debian-based
############

An automated installation script has been created for Debian-based distributions (e.g. Linux Mint and Ubuntu). You can implement the script with the following command::

  curl -sL https://raw.githubusercontent.com/aniketpanjwani/chomper_installers/master/debian.sh | bash && source ~/.bashrc

Enter your password where prompted. The script will install all UNIX dependencies, install pyenv (a Python version manager) and put it on PATH, install Python 3.6.4 in ~/.pyenv/ subdirectory, clone Chomper into ~/chomper, and append a Chomper executable to your PATH.

################
Non Debian-based
################

There is no automated installation yet for non Debian-based distributions. If you are interested in installing Chomper on your non Debian-based distribution, I suggest looking at the `automated installation script <https://github.com/aniketpanjwani/chomper_installers/blob/master/debian.sh>`__ for guidance.

If you are on a non-Debian based distribution, want to install Chomper, and are willing to create an installation script for your non-Debian based distribution, please create a new Issue in `Github Issues <https://github.com/aniketpanjwani/chomper/issues>`__. I would be happy to schedule a time for us to work together to get Chomper up and running on your distribution.
