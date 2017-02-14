#!/usr/bin/env python
# pylint: disable=no-member
"""
Runs pylint on all contained python files in this directory, printint out
nice colorized warnings/errors without all the other report fluff
"""
from __future__ import print_function
import os
import sys
import colorama
import pylint
import pylint.lint


__author__ = "Matthew 'MasterOdin' Peveler"
__license__ = "The MIT License (MIT)"

IGNORE_FOLDERS = [".git", ".idea", "__pycache__"]
ARGS = ["--reports=n", "--output-format=colorized", "--disable=locally-disabled"]

colorama.init(autoreset=True)


def runner(output=None, error=None):
    """
    Runs pylint on all python files in the current directory
    """

    pylint_output = output if output is not None else sys.stdout
    pylint_error = error if error is not None else sys.stderr
    savedout, savederr = sys.__stdout__, sys.__stderr__
    sys.stdout = pylint_output
    sys.stderr = pylint_error

    pylint_files = get_files_from_dir(os.curdir)
    version = '.'.join([str(x) for x in sys.version_info[0:3]])
    print("Using pylint " + colorama.Fore.RED + pylint.__version__ +
          colorama.Fore.RESET + " for python " + colorama.Fore.RED +
          version + colorama.Fore.RESET)
    print("pylint running on the following files:")
    for pylint_file in pylint_files:
        split_file = pylint_file.split("/")
        split_file[-1] = colorama.Fore.CYAN + split_file[-1] + colorama.Fore.RESET
        pylint_file = '/'.join(split_file)
        print("- " + pylint_file)
    print("----")

    run = pylint.lint.Run(ARGS + pylint_files, exit=False)

    sys.stdout = savedout
    sys.stderr = savederr

    sys.exit(run.linter.msg_status)


def get_files_from_dir(current_dir):
    """
    Recursively walk through a directory and get all python files and then walk
    through any potential directories that are found off current directory,
    so long as not within IGNORE_FOLDERS
    :return: all python files that were found off current_dir
    """
    if current_dir[-1] != "/" and current_dir != ".":
        current_dir += "/"
    files = []
    for dir_file in os.listdir(current_dir):
        if current_dir != ".":
            file_path = current_dir + dir_file
        else:
            file_path = dir_file
        if os.path.isfile(file_path):
            file_split = os.path.splitext(dir_file)
            if len(file_split) == 2 and file_split[0] != "" \
                    and file_split[1] == '.py':
                files.append(file_path)
        elif (os.path.isdir(dir_file) or os.path.isdir(file_path)) and dir_file not in IGNORE_FOLDERS:
            path = dir_file + "/"
            if current_dir != "" and current_dir != ".":
                path = current_dir.rstrip("/") + "/" + path
            files += get_files_from_dir(path)
    return files
