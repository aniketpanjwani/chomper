Installation
============

Chomper can be installed on any Linux distribution, but the installation has only been fully automated for Debian-based distributions.

For each installation method, you will need to be using a user with sudo privileges.

############
Debian-based
############

An automated installation script has been created for Debian-based distributions. You can view the script `here <https://gist.github.com/aniketpanjwani/bab67be0e685b65c13a6ec1cc132e321>`_. You can implement the script with the following command (using a shortened URL)::

  curl -sL https://git.io/vxORB | bash

Enter your password where prompted. The script will install all UNIX dependencies, install pyenv (a Python version manager) and put it on PATH, install Python 3.6.4 in ~/.pyenv/ subdirectory, clone Chomper into ~/chomper, and append a Chomper executable to your PATH.

################
Non Debian-based
################

Coming soon!
