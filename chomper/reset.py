# Copyright: (c) 2018, Aniket Panjwani <aniket.panjwani@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Reset NAT/Processes."""

import utils


def main():
    utils.reset_nat()
    utils.kill_process()


if __name__ == "__main__":
    main()
