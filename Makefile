# Copyright: (c) 2018, Aniket Panjwani <aniket@addictedto.tech>
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
	pipenv run mitmdump & sleep 2 && kill -9 $$! # Generate certificates
	openssl x509 -outform der -in ~/.mitmproxy/mitmproxy-ca.pem -out ~/.mitmproxy/mitmproxy-ca.crt
	sudo cp /home/$(CURRENT_USER)/.mitmproxy/mitmproxy-ca.crt /usr/local/share/ca-certificates/mitmproxy-ca.crt # Install root certificates
	sudo update-ca-certificates
	sudo sh ./chomper/certs.sh # Make browsers recognize root certificates
	sudo sysctl -w net.ipv4.ip_forward=1 # Enable ipv4 forwarding
	sudo sysctl -w net.ipv6.conf.all.forwarding=1 # Enable ipv6 forwarding
	sudo sysctl -p # Lock in new ip forwarding settings.

lock:
	echo $(SUDOERS_ENTRY) | sudo EDITOR='tee' visudo -f $(SUDOERS_FILE)
	sudo chown -R root:root ./
	sudo chown $(CURRENT_USER):$(CURRENT_USER) ./data/rules.yaml
	sudo chown $(CURRENT_USER):$(CURRENT_USER) ./readme.org
	sudo chown $(CURRENT_USER):$(CURRENT_USER) ./.gitignore
	sudo chown -R $(CURRENT_USER):$(CURRENT_USER) ./.git

reset:
	sudo env PATH=$(PATH) ${INTERPRETER}3.6m ${CURRENT_DIR}/chomper/reset.py
