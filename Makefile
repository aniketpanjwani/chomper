# Copyright: (c) 2018, Aniket Panjwani <aniket.panjwani@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

SHELL:=/bin/bash
INTERPRETER=$(shell pipenv --py)
CURRENT_USER:=$(shell whoami)
CURRENT_DIR:=$(shell pwd)
SUDOERS_FILE:=/etc/sudoers.d/chomper
SUDOERS_ENTRY_MIDDLE:=" ALL=(ALL) NOPASSWD: "
SUDOERS_ENTRY_SUFFIX:="/chomper/block.py *"
SUDOERS_ENTRY:=$(CURRENT_USER)$(SUDOERS_ENTRY_MIDDLE)$(INTERPRETER) $(CURRENT_DIR)$(SUDOERS_ENTRY_SUFFIX)

init:
	pip install pipenv # Install pipenv
	pipenv install --dev # Install packages

lock:
	echo $(SUDOERS_ENTRY) | sudo EDITOR='tee -a' visudo -f $(SUDOERS_FILE)
	sudo chown -R root:root ./
	sudo chown $(CURRENT_USER):$(CURRENT_USER) ./data/rules.yaml
	sudo chown $(CURRENT_USER):$(CURRENT_USER) ./readme.org
	sudo chown $(CURRENT_USER):$(CURRENT_USER) ./readme.org
	sudo chown $(CURRENT_USER):$(CURRENT_USER) ./.gitignore
	sudo chown -R $(CURRENT_USER):$(CURRENT_USER) ./.git

reset:
	sudo env PATH=$(PATH) ${INTERPRETER}3.6m ${CURRENT_DIR}/chomper/reset.py
