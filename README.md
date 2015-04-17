#pylint_runner
[![Build Status](https://travis-ci.org/MasterOdin/pylint_runner.svg?branch=master)](https://travis-ci.org/MasterOdin/pylint_runner)
[![Coverage Status](https://coveralls.io/repos/MasterOdin/pylint_runner/badge.svg?branch=master)](https://coveralls.io/r/MasterOdin/pylint_runner?branch=master)
[![Latest Version](https://pypip.in/version/pylint_runner/badge.svg?text=pypi)](https://pypi.python.org/pypi/pylint_runner/)
[![Supported Python versions](https://pypip.in/py_versions/pylint_runner/badge.svg)](https://pypi.python.org/pypi/pylint_runner/)
[![License](https://pypip.in/license/pylint_runner/badge.svg)](https://pypi.python.org/pypi/pylint_runner/)

A simple pylint application that runs scans the current directory and any sub-directories recursively, then runs pylint on all discovered .py files.

##Installation
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

##Usage
```
pylint_runner
```

This will generate (if run against this repo):  
```
Using pylint 1.4.1 for python 2.7.8  
pylint running on the following files:
- ./pylint_runner/__init__.py
- ./pylint_runner/main.py
- ./setup.py
- ./tests/__init__.py
- ./tests/test_runner.py
----
No config file found, using default configuration
```

If there were any issues, the following would be attached to the above print:
```
************* Module pylint_runner.main
C: 24, 0: Missing function docstring (missing-docstring)
************* Module tests.test_runner
C: 19, 0: Final newline missing (missing-final-newline)
C: 19, 0: Invalid constant name "a" (invalid-name)
```