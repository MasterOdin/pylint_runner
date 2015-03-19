# pylint: disable=missing-docstring,no-value-for-parameter
import os
import pylint_runner.main as runner
from nose.tools import assert_raises, assert_equal


def test_get_files():
    # make sure we use root of pylint_runner module
    os.chdir(os.path.dirname(os.path.realpath(__file__)) + '/../')
    actual = runner.get_files_from_dir(os.curdir)
    expected = ['pylint_runner/__init__.py', 'pylint_runner/main.py',
                'setup.py', 'tests/__init__.py', 'tests/test_runner.py',
                'tests/tests/dummy.py']
    assert_equal(sorted(expected), sorted(actual))


def test_runner():
    with assert_raises(SystemExit) as context_manager:
        runner.runner(error=open(os.devnull, 'w'))
    assert_equal(context_manager.exception.code, 0)
