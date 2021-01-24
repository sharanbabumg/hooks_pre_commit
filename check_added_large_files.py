#!/usr/bin/env python3
import argparse
import json
import math
import os
from typing import Optional
from typing import Sequence

from util import added_files


def find_large_added_files(maxkb: int) -> int:
    # Find all added files that are also in the list of files pre-commit tells
    # us about
    retv = 0

    filenames = added_files()

    for filename in filenames:
        kb = int(math.ceil(os.stat(filename).st_size / 1024))
        if kb > maxkb:
            print(f'{filename} ({kb} KB) exceeds {maxkb} KB.')
            retv = 1

    return retv


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--maxkb', type=int, default=500,
        help='Maxmimum allowable KB for added files',
    )
    args = parser.parse_args(argv)

    return find_large_added_files(args.maxkb)


if __name__ == '__main__':
    exit(main())
