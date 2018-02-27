# Copyright: (c) 2018, Aniket Panjwani <aniket@addictedto.tech>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Based off of script by Thomas Leister (https://thomas-leister.de/en/how-to-import-ca-root-certificate/)
# MIT Licensed here: https://github.com/ThomasLeister/root-certificate-deployment

#!/bin/bash

### Script installs mitmproxy certificate to certificate trust store of applications using NSS
### (e.g. Firefox, Thunderbird, Chromium)
### Mozilla uses cert8, Chromium and Chrome use cert9

###
### Requirement: apt install libnss3-tools
###


###
### For cert8 (legacy - DBM)
###

for certDB in $(find ~/ -name "cert8.db")
do
    certdir=$(dirname ${certDB});
    certutil -A -n "Chomper" -t "TCu,Cu,Tu" -i $1 -d dbm:${certdir}
done


###
### For cert9 (SQL)
###

for certDB in $(find ~/ -name "cert9.db")
do
    certdir=$(dirname ${certDB});
    certutil -A -n "Chomper" -t "TCu,Cu,Tu" -i $1 -d sql:${certdir}
done
