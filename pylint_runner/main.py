#!/usr/bin/env python
"""
Runs pylint on all contained python files in this directory, printint out
nice colorized warnings/errors without all the other report fluff
"""
from __future__ import print_function

import os
import sys
from argparse import ArgumentParser
import colorama
import pylint
import pylint.lint

from pylint_runner import __version__

if sys.version_info > (3,):
    PY2 = False
else:
    PY2 = True
if PY2:
    # noinspection PyCompatibility,PyPep8Naming,PyUnresolvedReferences
    # pylint: disable=import-error
    import ConfigParser as configparser
else:
    # noinspection PyCompatibility
    # pylint: disable=import-error
    import configparser

PYTHON_VERSION = '.'.join([str(x) for x in sys.version_info[0:3]])


class Runner(object):
    """ A pylint runner that will lint all files recursively from the CWD. """

    DEFAULT_IGNORE_FOLDERS = [".git", ".idea", "__pycache__"]
    DEFAULT_ARGS = ["--reports=n", "--output-format=colorized"]
    DEFAULT_RCFILE = '.pylintrc'

    def __init__(self, args=None):
        colorama.init(autoreset=True)

        self.verbose = False
        self.args = self.DEFAULT_ARGS
        self.rcfile = self.DEFAULT_RCFILE
        self.ignore_folders = self.DEFAULT_IGNORE_FOLDERS

        self._parse_args(args or sys.argv[1:])
        self._parse_ignores()

    def _parse_args(self, args):
        """Parses any supplied command-line args and provides help text. """

        parser = ArgumentParser(description='Runs pylint recursively on a directory')

        parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                            help='Verbose mode (report which files were found for testing).')

        parser.add_argument('--rcfile', dest='rcfile', action='store', default='.pylintrc',
                            help='A relative or absolute path to your pylint rcfile. Defaults to\
                            `.pylintrc` at the current working directory')

        parser.add_argument('-V', '--version', action='version',
                            version="%(prog)s ({0}) for Python {1}".format(__version__,
                                                                           PYTHON_VERSION))

        options, _ = parser.parse_known_args(args)

        self.verbose = options.verbose

        if options.rcfile:
            if not os.path.isfile(options.rcfile):
                options.rcfile = os.getcwd() + '/' + options.rcfile
            self.rcfile = options.rcfile

        return options

    def _parse_ignores(self):
        """ Parse the ignores setting from the pylintrc file if available. """

        error_message = (
            colorama.Fore.RED +
            '{} does not appear to be a valid pylintrc file'.format(self.rcfile) +
            colorama.Fore.RESET
        )

        if not os.path.isfile(self.rcfile):
            if not self._is_using_default_rcfile():
                print(error_message)
                sys.exit(1)
            else:
                return

        config = configparser.ConfigParser()
        try:
            config.read(self.rcfile)
        except configparser.MissingSectionHeaderError:
            print(error_message)
            sys.exit(1)

        if config.has_section('MASTER') and config.get('MASTER', 'ignore'):
            self.ignore_folders += config.get('MASTER', 'ignore').split(',')

    def _is_using_default_rcfile(self):
        return self.rcfile == os.getcwd() + '/' + self.DEFAULT_RCFILE

    def _print_line(self, line):
        """ Print output only with verbose flag. """
        if self.verbose:
            print(line)

    def get_files_from_dir(self, current_dir):
        """
        Recursively walk through a directory and get all python files and then walk
        through any potential directories that are found off current directory,
        so long as not within self.IGNORE_FOLDERS
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
            elif (os.path.isdir(dir_file) or os.path.isdir(file_path))\
                    and dir_file not in self.ignore_folders:
                path = dir_file + os.path.sep
                if current_dir != "" and current_dir != ".":
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
        self._print_line("Using pylint " + colorama.Fore.RED + pylint.__version__ +
                         colorama.Fore.RESET + " for python " + colorama.Fore.RED +
                         PYTHON_VERSION + colorama.Fore.RESET)

        self._print_line("pylint running on the following files:")
        for pylint_file in pylint_files:
            # we need to recast this as a string, else pylint enters an endless recursion
            split_file = str(pylint_file).split("/")
            split_file[-1] = colorama.Fore.CYAN + split_file[-1] + colorama.Fore.RESET
            pylint_file = '/'.join(split_file)
            self._print_line("- " + pylint_file)
        self._print_line("----")

        if not self._is_using_default_rcfile():
            self.args += ['--rcfile={}'.format(self.rcfile)]

        run = pylint.lint.Run(self.args + pylint_files, exit=False)
        sys.stdout = savedout
        sys.stderr = savederr

        sys.exit(run.linter.msg_status)


def main(output=None, error=None, verbose=False):
    """ The main (cli) interface for the pylint runner. """
    runner = Runner(args=["--verbose"] if verbose is not False else None)
    runner.run(output, error)

if __name__ == "__main__":
    main(verbose=True)
