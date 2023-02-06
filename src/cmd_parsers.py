import argparse

from src.descriptions import PROGRAM_NAME, SHORT_INFO, HELP_INFO
from src.exceptions import ArgumentNotFoundError


def parse_cmd():
    parser = argparse.ArgumentParser(prog=PROGRAM_NAME,
                                     description=SHORT_INFO,
                                     epilog=HELP_INFO)
    parser.add_argument("-f", "--file", required=False)
    args = parser.parse_args()
    if not args.file:
        raise ArgumentNotFoundError("--file")
    else:
        return args.file
