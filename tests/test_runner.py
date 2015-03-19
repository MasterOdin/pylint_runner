# pylint: disable=missing-docstring,no-value-for-parameter
import os
import pylint_runner.main as runner
from nose.tools import assert_raises, assert_equal


def test_get_files():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    actual = runner.get_files_from_dir(cur_dir)
    expected = [cur_dir+'/__init__.py', cur_dir+'/test_runner.py']
    assert_equal(sorted(expected), sorted(actual))


def test_runner():
    with assert_raises(SystemExit) as context_manager:
        runner.runner(error=open(os.devnull, 'w'))
    assert_equal(context_manager.exception.code, 0)
