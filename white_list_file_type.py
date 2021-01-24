#!/usr/bin/env python3
import argparse
import os
from typing import Optional
from typing import Sequence

from util import added_files


def find_filetypes(filetypes: int) -> int:
    # Find all added files that are also in the list of files pre-commit tells
    # us about
    retv = 0

    filenames = added_files()

    for filename in filenames:
        _, ext = os.path.splitext(filename)
        if ext not in filetypes:
            print(f'{filename} that contains {ext} extensions are not allowed.')
            retv = 1
    return retv


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--filetypes', type=list, default=[".py", ".yaml", ".yml"],
        help='Allowed file types',
    )
    args = parser.parse_args(argv)

    return find_filetypes(args.filetypes)


if __name__ == '__main__':
    exit(main())
