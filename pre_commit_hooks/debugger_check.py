import argparse
from typing import Sequence

def check_file(filename: str) -> bool:
    with open(filename, mode='rb') as file:
        lines = file.readlines()
    return_code = 0
    for line in lines:
        if check_line(line):
            return_code = 1
    return return_code

def check_line(line: bytes) -> bool:
    if b'debugger;' in line:
        return 1
    return 0

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)
    return_code = 0
    for filename in args.filenames:
        if filename[-3:] == '.js' and check_file(filename):
            print(f'debugger in {filename}')
            return_code = 1
    return return_code