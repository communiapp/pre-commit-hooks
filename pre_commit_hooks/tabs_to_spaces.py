import argparse
from typing import Sequence

def check_file(filename: str) -> bool:
    with open(filename, mode='rb') as file:
        lines = file.readlines()
    newfile = ""
    fixed_tabs = 0
    for line in lines:
        if b"\t" in line:
            fixed_tabs = fixed_tabs + 1
        newfile = newfile + line.replace(b"\t", bytes("    ")) + "\n"
    file.close()
    file_out = open(filename, mode='wb')
    file_out.write(newfile)
    file_out.close()
    return fixed_tabs

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)
    for filename in args.filenames:
        fixed_tabs = check_file(filename)
        if fixed_tabs:
            print(f'{fixed_tabs} fixed tabs in {filename}')
    return 0