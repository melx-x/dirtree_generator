from . import __version__
from argparse import ArgumentParser
from .dirtree_generator import DirectoryTree
import pathlib
import sys 

def main():
    args = parse_cmd_line_arguments()
    dir = pathlib.Path(args.dir)
    if not dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    tree = DirectoryTree(dir, dir_only=args.dir_only, output_file=args.output_file)
    tree.generate()
    

def parse_cmd_line_arguments():
    parser = ArgumentParser(
        prog="tree",
        description=" DirTree Genertor, a directory tree generator",
        epilog="Thanks for using  DirTree Generator!"
    )
    parser.version  = f"DirTree Generator v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "dir",
        metavar="DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at DIR",
    )
    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="Generate a directory-only tree",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        metavar="OUTPUT_FILE",
        nargs="?",
        default=sys.stdout,
        help="Generate a full directory tree and save it to a file",
    )
    return parser.parse_args()