# Copyright: (c) 2018, Aniket Panjwani <aniket@addictedto.tech>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
MITMDUMP_COMMAND = 'screen -d -m {} --set allow_remote=true --mode transparent --showhost -s ./chomper/filter.py --set "addresses_str={}" --set "block_type={}" --set "rule_name={}" --set "block_end_time={}"'
