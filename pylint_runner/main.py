#!/usr/bin/env python
"""
Runs pylint on all contained python files in this directory, printint out
nice colorized warnings/errors without all the other report fluff
"""

from argparse import ArgumentParser
import configparser
import os
import sys

import colorama
import pylint
import pylint.lint
from pylint.lint.pylinter import PyLinter

from pylint_runner import __version__

PYTHON_VERSION = ".".join([str(x) for x in sys.version_info[0:3]])


class Runner:
    """ A pylint runner that will lint all files recursively from the CWD. """

    DEFAULT_IGNORE_FOLDERS = [".git", ".idea", "__pycache__"]
    DEFAULT_ARGS = ["--reports=n", "--output-format=colorized"]

    def __init__(self, args=None):
        if args is None:
            args = []

        colorama.init(autoreset=True)

        self.verbose = False
        self.args = list(self.DEFAULT_ARGS)
        self.rcfile = None
        self.ignore_folders = self.DEFAULT_IGNORE_FOLDERS

        self._parse_args(args)
        self._parse_ignores()

    def _parse_args(self, args):
        """Parses any supplied command-line args and provides help text. """

        parser = ArgumentParser(
            description="Runs pylint recursively on a directory"
        )

        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            action="store_true",
            default=False,
            help="Verbose mode (report which files were found for testing).",
        )

        parser.add_argument(
            "--rcfile",
            dest="rcfile",
            action="store",
            help="A relative or absolute path to your pylint rcfile.",
        )

        parser.add_argument(
            "-V",
            "--version",
            action="version",
            version="%(prog)s ({0}) for Python {1}".format(
                __version__,
                PYTHON_VERSION
            ),
        )

        options, rest = parser.parse_known_args(args)

        self.verbose = options.verbose

        self.rcfile = options.rcfile

        self.args += rest

        return options

    def _parse_ignores(self):
        """ Parse the ignores setting from the pylintrc file if available. """

        error_message = (
            colorama.Fore.RED
            + "{} does not appear to be a valid pylintrc file".format(
                self.rcfile
            )
            + colorama.Fore.RESET
        )

        if self.rcfile is not None and not os.path.isfile(self.rcfile):
            print(error_message)
            sys.exit(1)

        linter = PyLinter(pylintrc=self.rcfile)
        try:
            linter.read_config_file()
        except configparser.MissingSectionHeaderError:
            print(error_message)
            sys.exit(1)

        config = linter.cfgfile_parser
        if config.has_option("MASTER", "ignore"):
            self.ignore_folders += config.get("MASTER", "ignore").split(",")

    def _print_line(self, line):
        """ Print output only with verbose flag. """
        if self.verbose:
            print(line)

    def get_files_from_dir(self, current_dir):
        """
        Recursively walk through a directory and get all python files and then
        walk through any potential directories that are found off current
        directory, so long as not within self.IGNORE_FOLDERS
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
                        and file_split[1] == ".py":
                    files.append(file_path)
            elif (os.path.isdir(dir_file) or os.path.isdir(file_path)) \
                    and dir_file not in self.ignore_folders:
                path = dir_file + os.path.sep
                if current_dir not in ["", "."]:
                    path = os.path.join(current_dir.rstrip(os.path.sep), path)
                files += self.get_files_from_dir(path)
        return files

    def run(self, output=None, error=None):
        """ Runs pylint on all python files in the current directory """

        pylint_output = output if output is not None else sys.stdout
        pylint_error = error if error is not None else sys.stderr
        savedout, savederr = sys.__stdout__, sys.__stderr__
        sys.stdout = pylint_output
        sys.stderr = pylint_error

        pylint_files = self.get_files_from_dir(os.curdir)
        print(
            "Using pylint "
            + colorama.Fore.RED
            + pylint.__version__
            + colorama.Fore.RESET
            + " for python "
            + colorama.Fore.RED
            + PYTHON_VERSION
            + colorama.Fore.RESET,
            file=sys.stdout
        )

        self._print_line("pylint running on the following files:")
        for pylint_file in pylint_files:
            # we need to recast this as a string, else pylint enters an
            # endless recursion
            split_file = str(pylint_file).split("/")
            split_file[-1] = colorama.Fore.CYAN + split_file[-1] \
                + colorama.Fore.RESET
            pylint_file = "/".join(split_file)
            self._print_line("- " + pylint_file)
        self._print_line("----")

        if self.rcfile is not None:
            # insert this at the front so it's not after any potential
            # positional arguments
            self.args.insert(0, "--rcfile={}".format(self.rcfile))

        pylint_version = [int(x) for x in pylint.__version__.split('.')]

        pylint_5 = pylint_version[1] == 5 and pylint_version[2] < 1
        pylint_pre_5 = pylint_version[1] < 5

        if pylint_version[0] >= 2 and (pylint_pre_5 or pylint_5):
            exit_kwarg = {"do_exit": False}
        else:
            exit_kwarg = {"exit": False}

        run = pylint.lint.Run(self.args + pylint_files, **exit_kwarg)
        sys.stdout = savedout
        sys.stderr = savederr

        sys.exit(run.linter.msg_status)


def main(output=None, error=None, verbose=False, args=None):
    """ The main (cli) interface for the pylint runner. """
    if args is None:
        args = sys.argv[1:]
    if verbose and '--verbose' not in args:
        args.insert(0, '--verbose')
    runner = Runner(args)
    runner.run(output, error)


if __name__ == "__main__":
    main(verbose=True)
