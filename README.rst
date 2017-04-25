pylint_runner
=============

.. image:: https://travis-ci.org/MasterOdin/pylint_runner.svg?branch=master
    :target: https://travis-ci.org/MasterOdin/pylint_runner
    :alt: Build Status
.. image:: https://coveralls.io/repos/MasterOdin/pylint_runner/badge.svg?branch=master
    :target: https://coveralls.io/r/MasterOdin/pylint_runner?branch=master
    :alt: Coverage Status
.. image:: https://img.shields.io/pypi/v/pylint_runner.svg
    :target: https://pypi.python.org/pypi/pylint_runner/
    :alt: PyPI Version
.. image:: https://img.shields.io/pypi/pyversions/pylint_runner.svg
    :target: https://pypi.python.org/pypi/pylint_runner/
    :alt: Supported Python Versions
.. image:: https://img.shields.io/github/license/MasterOdin/pylint_runner.svg
    :target: https://github.com/MasterOdin/pylint_runner/blob/master/LICENSE
    :alt: License

A simple pylint application that scans the current directory and any sub-directories recursively,
then runs pylint on all discovered `.py` files.

Dependencies
------------

- `colorama <https://pypi.python.org/pypi/colorama>`_
- `pylint <https://pypi.python.org/pypi/pylint>`_
- `nose <https://pypi.python.org/pypi/nose>`_ (for testing)

Installation
------------

Preferred installation method::

    pip install pylint_runner

From source::

    python setup.py install

When installed, this will create an executable `pylint_runner`, `pylint_runner#`, and `pylint_runner#.#`
where the first # represents the major version of Python (2 or 3) and the second # represents the minor
version of Python. So if installed by Python 2.7, you will have available `pylint_runner`, `pylint_runner2`,
and `pylint_runner2.7` so as to allow usage by however many installed versions of python on the system as
pylint is version dependent on its output (due to using the Python AST).

Usage
-----

::

    pylint_runner

Output is standard pylint output. There should be no output if no issues were found.

In case of issues, you should see output similar to::

    ************* Module foo.bar
    C: 24, 0: Missing function docstring (missing-docstring)
    ************* Module tests.foo_tester
    C: 19, 0: Final newline missing (missing-final-newline)
    C: 19, 0: Invalid constant name "a" (invalid-name)

Additional Arguments

See the standard help ouput::

    pylint_runner -h

Verbose mode
------------
::

    pylint_runner -v

Verbose mode lists all files that were found for testing immediately, along with the pylint output.

This will generate (if run against this repo)::

    Using pylint 1.6.5 for python 2.7.11
    pylint running on the following files:
    - pylint_runner/__init__.py
    - pylint_runner/main.py
    - setup.py
    - tests/__init__.py
    - tests/test_runner.py
    - tests/tests/dummy.py

    ************* Module tests.test_runner
    I:  1, 0: Locally disabling missing-docstring (C0111) (locally-disabled)

rcfile
------

This allows you to specify a pylintrc file to be used using `--rcfile path\_to\_file`.

It may be a relative, or absolute path and defaults to `.pylintrc` at the current working directory.

It will read the value of `ignore` from the rcfile and ignore any matching files/folders while building the list of
files to pass to python.

It will also pass that rcfile for use by pylint.
