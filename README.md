# pylint_runner
[![Build Status](https://travis-ci.org/MasterOdin/pylint_runner.svg?branch=master)](https://travis-ci.org/MasterOdin/pylint_runner)
[![Coverage Status](https://coveralls.io/repos/MasterOdin/pylint_runner/badge.svg?branch=master)](https://coveralls.io/r/MasterOdin/pylint_runner?branch=master)
[![PyPI version](https://img.shields.io/pypi/v/pylint_runner.svg)](https://pypi.python.org/pypi/pylint_runner/)
[![Supported Python versions](https://img.shields.io/badge/python%20version-2.6%2B%2C%203.2%2B-brightgreen.svg)](https://pypi.python.org/pypi/pylint_runner/)
[![License](https://img.shields.io/github/license/MasterOdin/pylint_runner.svg)](https://github.com/MasterOdin/pylint_runner/)

A simple pylint application that scans the current directory and any sub-directories recursively, then runs pylint on all discovered `.py` files.

## Installation
Dependencies:  
* [colorama](https://pypi.python.org/pypi/colorama)  
* [pylint](http://www.pylint.org/)  
* [nose](https://nose.readthedocs.org/en/latest/) (for testing)

Preferred installation method:
```shell
pip install pylint_runner
```

From source:
```shell
python setup.py install
```

## Usage

```shell
pylint_runner
```

Output is standard pylint output. There should be no output if no issues were found.

In case of issues, you should see output similar to:

```
************* Module pylint_runner.main
C: 24, 0: Missing function docstring (missing-docstring)
************* Module tests.test_runner
C: 19, 0: Final newline missing (missing-final-newline)
C: 19, 0: Invalid constant name "a" (invalid-name)
```

### Additional Arguments

See the standard help ouput:

```shell
pylint_runner -h
```

#### Verbose mode

```shell
pylint_runner -v
```
Verbose mode lists all files that were found for testing immediately, along with the pylint output.

This will generate (if run against this repo): 
 
```
Using pylint 1.6.5 for python 2.7.11
pylint running on the following files:
- pylint_runner/__init__.py
- pylint_runner/main.py
- setup.py
- tests/__init__.py
- tests/test_runner.py
- tests/tests/dummy.py
----
************* Module tests.test_runner
I:  1, 0: Locally disabling missing-docstring (C0111) (locally-disabled)
```

#### --rcfile path\_to\_file

This allows you to specify a pylintrc file to be used.

It may be a relative, or absolute path and defaults to `.pylintrc` at the current working directory.

It will read the value of `ignore` from the rcfile and ignore any matching files/folders while building the list of files to pass to python.

It will also pass that rcfile for use by pylint.
