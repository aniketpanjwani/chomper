Advanced Usage
==============

#############
Hardcore Mode
#############

If you use Linux and have root privileges, it is impossible to prevent yourself from breaking any sort of Internet block. If you want to use Chomper seriously, I suggest you do the following:

#. Create a new account with administrative privileges. Give this account a very long, complicated password. Write down the password, and store it in some secure, but difficult to access location.
#. While your main account still has root privileges, run ``make lock`` from the base directory and enter your password where prompted.
#. Remove your main account's administrative privileges, log out, and log back in.

You will now be able to use Chomper using the ``chomper`` executable the ``bin`` directory, but you will not be able to edit the code, or kill any processes started by Chomper to block websites.

If you want to keep a back-door which allows you to have delayed access to root privileges, I suggest the nifty `delayed-admin tool <https://github.com/miheerdew/delayed-admin>`__.
