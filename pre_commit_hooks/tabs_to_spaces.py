import argparse
from typing import Sequence

def check_file(filename: str) -> bool:
    with open(filename, mode='r') as file:
        content = file.read()
    newcontent = content.replace("\t", "    ")
    with open(filename, mode='w') as file:
        file.write(newcontent)
    return newcontent != content

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)
    for filename in args.filenames:
        if (filename.lower().endswith(('.css', '.dist', '.htm', '.html', '.js', '.json', '.less', '.md', '.php', '.xml', '.yaml', '.yml'))):
            fixed_tabs = check_file(filename)
            if fixed_tabs:
                print(f'Fixed tabs in {filename}')
    return 0