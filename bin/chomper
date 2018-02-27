# Copyright: (c) 2018, Aniket Panjwani <aniket@addictedto.tech>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#!/bin/bash
SCRIPT=$(readlink -f "$0")
CURRENTDIR=$(dirname "$SCRIPT")
PROJECTDIR=$(dirname "$CURRENTDIR")
cd $PROJECTDIR && INTERPRETER=$(pipenv --py)
cd $PROJECTDIR && MITMDUMP_BIN_PATH=$(pipenv --venv)/bin/mitmdump
CURRENT_USER=$(whoami)

PATH=${PATH}:/sbin:/usr/sbin
if ! hash iptables 2>/dev/null; then
   echo "ERROR: iptables not found in \$PATH\n"
   echo "PATH=${PATH}"
   exit 1
fi

sudo ${INTERPRETER} ${PROJECTDIR}/chomper/block.py --rule=$1 --block_length=$2 --settings_json_path=${PROJECTDIR}/data/block_settings.json --reset_command "env PATH=${PATH} ${INTERPRETER} ${PROJECTDIR}/chomper/reset.py" --mitmdump_bin_path=${MITMDUMP_BIN_PATH}
