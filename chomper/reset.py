"""Reset NAT/Processes."""

import utils


def main():
    utils.reset_nat()
    utils.kill_process()


if __name__ == "__main__":
    main()
