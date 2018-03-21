Development
===========

This section describes the Chomper code base for developers interested in contributing to Chomper.

########
Overview
########

Chomper is a wrapper around a Python proxy library called `mitmproxy <https://mitmproxy.org>`_. When the :code:`chomper` executable is called with arguments :code:`rule-name` and :code:`block-time`, the Python interpreter in calls :code:`./chomper/block.py` to enact a block.

:code:`./chomper/block.py` first checks to see if a block is in effect by reading :code:`./data/block_settings.json`.

1. If a block is not in effect,
   1. Set a new block (using :code:`chomper.block.enact_block`).
   2. Create a new set of block settings (using :code:`chomper.block.create_block_dict`).
   3. Schedule a task on root's Crontab to remove the block in :code:`block-time` minutes by calling :code:`./chomper/reset.py`.
   4. Provide a message informing users that a new block has been enacted, and tell them when the block will end.
2. If a block is in effect,
   1. Reinstate the old block.
   2. Provide a message informing users that the old block is still in effect, and tell them when the block will end.

#################################
:code:`chomper.block.enact_block`
#################################
This function enacts new blocks. It does the following:

1. 
