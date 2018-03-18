Basic Usage
===========

When using Chomper, you define *rules* of websites to blacklist or whitelist in a YAML file. Blocks are then executed using selected rules for a number of minutes specified by the user.

##############
Types of Rules
##############

A rule can either be a blacklist or a whitelist

* blacklist: a set of websites which you cannot go to
* whitelist: an exclusive set of websites which you can go to

A rule is composed of addresses, which can be

* domains: e.g. facebook.com
* subdomains: e.g. unix.stackexchange.com
* URLS: e.g. github.com/coleifer/peewee

For example, if unix.stackexchange.com is part of a whitelist rule named *coding*, when *coding* is executed, the user will be able to go to unix.stackexchange.com, but will not be able to go to aviation.stackexchange.com.

##################
Configuration File
##################

Chomper's rules are configured through a simple YAML file located at ./chomper/data/rules.yaml. The first level specifies the names of the rules. The second level defines whether a rule is a blacklist or whitelist, and the addresses involved in a rule. An example configuration file is found below

.. code:: yaml

    coding:
      - block_type:
          - whitelist
      - addresses:
        - stackoverflow.com
        - unix.stackexchange.com
        - python.org
    nosocial:
      - block_type:
          - blacklist
      - addresses:
          - facebook.com
          - instagram.com
          - twitter.com
    allon:
      - block_type:
          - blacklist
      - addresses:
          - abcdxyz.com
    alloff:
      - block_type:
          - whitelist 
      - addresses:
          - abcdxyz.com

The last two rules, *allon* and *alloff*, are ad-hoc implementations to either allow or block all websites.

################
Executing Blocks
################

Blocks are executed through the syntax :code:`chomper rule_name num_minutes`

For example, with the above YAML file,

* :code:`chomper coding 10` will allow you to only visit those websites under the *coding* rule for 10 minutes
* :code:`chomper nosocial 20` will allow you to visit all websites except those under the *nosocial* rule for 20 minutes

##################
Overlapping Blocks
##################

When you execute a block, you are locked in to that block. If you try to execute a new block while a block is in progress, you will be prevented from executing the new block.

#################
Resetting a Block
#################

If you have administrator privileges, you can execute :code:`make reset` from the ./chomper directory. This will restore your Internet access to normal.

However, be wary of the following possibility:

1. You set a block at 11:00 A.M. for 30 minutes.
2. At 11:15 A.M., you reset the block with :code:`make reset`.
3. If, at 11:20 A.M., you try to set a new block, instead, your old block will be enacted (due to the overlapping blocks feature).
