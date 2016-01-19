#!/usr/bin/env python

description = """
Generic Script
--------------

This description should be formatted raw so that this text does not go off the
terminal when the '--help' flag is called.
"""

import sys
import argparse


def main(argv):
    args = cli(argv)


class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
    pass


def cli(argv):
    parser = argparse.ArgumentParser(
        prog=argv[0],
        description=description,
        formatter_class=CustomFormatter)

    parser.add_argument(
        "--flag",
        action='store_true',
        help="Flag help.")

    parser.add_argument(
        "--arg",
        required=False,
        type=str,
        default="value",
        help="Argument help.")

    group = parser.add_argument_group(title="argument group")

    group.add_argument(
        "--group_flag",
        action='store_true',
        help="Flag help.")

    group.add_argument(
        "--group_arg",
        metavar='ARG',
        required=False,
        type=str,
        default="value",
        help="Argument help.")

    args = parser.parse_args(argv[1:])

    return args


if __name__ == '__main__':
    sys.exit(main(sys.argv))
