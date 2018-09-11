# History

## 0.5.4 (09/12/2018)

* Fix break in function signature of pylint.lint.Run for Python 3+ (thanks cjhall1283)
* Mark this as the last release for Python 2.7 (will be removed in 0.6.0)

## 0.5.3 (04/16/2018)

* Remove official support of Python 2.6, 3.2, and 3.3

## 0.5.2 (04/14/2018)

* Remove dependency on pip

## 0.5.1 (02/27/2018)

* Mark Python 3.6 as supported

## 0.5.0 (04/25/2017)

* Added additional entry points to make it possible to have pylint_runner installed for multiple python versions

## 0.4.0 (03/13/2017)

* Refactored module into class to facilitate easy argument loading
* Added verbose mode and defaulted to off
* Added the ability to specify a pylintrc file (defaults to `.pylintrc` relative to calling location)
