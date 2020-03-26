from typing import Set
from os import path
import py_compile
import argparse
import shutil
import os


def is_python_file(file_path: str) -> bool:
    return file_path.endswith(".py")


def rename_python_file(file_path: str) -> str:
    return "{}c".format(file_path)


def main():

    parser = argparse.ArgumentParser(description="Script for compiling a project")
    parser.add_argument("src", help="Source directory of your project containing either python files to compile or resurce files")
    parser.add_argument("dst", help="Destination directory of compiled of copied files")
    parser.add_argument("-x", help="Excluded files or directories", nargs="+")
    parser.add_argument("-r", help="Excluded files or directories by names", nargs="+")
    args = parser.parse_args()

    process_dir(args.src, args.dst, {path.join(args.src, exfile) for exfile in args.x}, set(args.r))


def process_dir(src_dir: str, dst_dir: str, excluded: Set, excluded_names: Set):

    if not path.isdir(dst_dir):
        os.mkdir(dst_dir)

    for entry_name in os.listdir(src_dir):

        if entry_name in excluded_names:
            continue

        entry_src = path.join(src_dir, entry_name)
        entry_dst = path.join(dst_dir, entry_name)

        if entry_src in excluded:
            continue

        if path.isdir(entry_src):
            process_dir(entry_src, entry_dst, excluded, excluded_names)
        elif path.isfile(entry_src):

            if is_python_file(entry_src):

                entry_dst = rename_python_file(entry_dst)

                print("{} : compiling ...".format(entry_src))
                py_compile.compile(entry_src, cfile=entry_dst)
                print("{} : compiled !".format(entry_src))

            else:

                print("{} : copying ...".format(entry_src))
                shutil.copy2(entry_src, entry_dst)


if __name__ == "__main__":
    main()
