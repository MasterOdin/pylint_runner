# pylint: disable=missing-docstring
import os
import pytest
import pylint_runner.main as runner


def test_get_files():
    # make sure we use root of pylint_runner module
    os.chdir(os.path.dirname(os.path.realpath(__file__)) + '/../')
    actual = runner.Runner().get_files_from_dir(os.curdir)
    expected = [
        'pylint_runner/__init__.py',
        'pylint_runner/main.py',
        'setup.py',
        'tests/__init__.py',
        'tests/test_runner.py',
        'tests/tests/dummy.py'
    ]
    _assert_list_equals(expected, actual)


def test_get_files_current_dir():
    path = os.path.dirname(os.path.realpath(__file__))
    actual = runner.Runner().get_files_from_dir(path)
    expected = [
        path + '/__init__.py',
        path + '/test_runner.py',
        path + '/tests/dummy.py'
    ]
    _assert_list_equals(expected, actual)


def test_main():
    with pytest.raises(SystemExit) as excinfo:
        runner.main(error=open(os.devnull, 'w'))
    assert excinfo.value.code == 0


def test_rcparser_success():
    with pytest.raises(SystemExit) as excinfo:
        args = ['--rcfile', 'tests/tests/good_rc_file']
        the_runner = runner.Runner(args=args)
        the_runner.run(error=open(os.devnull, 'w'))
    assert excinfo.value.code == 0
    assert 'migrations' in the_runner.ignore_folders


def test_rcparser_failure():
    with pytest.raises(SystemExit) as excinfo:
        args = ['--rcfile', 'tests/tests/bad_rc_file']
        runner.Runner(args=args)
    assert excinfo.value.code == 1


def test_rcparser_bad_file():
    with pytest.raises(SystemExit) as excinfo:
        args = ['--rcfile', 'non-existant-file']
        runner.Runner(args=args)
    assert excinfo.value.code == 1


def _assert_list_equals(list1, list2):
    assert len(list1) == len(list2)
    assert sorted(list1) == sorted(list2)


def test_passthrough_args():
    the_runner = runner.Runner(args=['-d', 'C0103', '-d', 'E0602'])
    expected = [
        '--rcfile=tests/tests/good_rc_file',
        '--rcfile=.pylintrc',
        '--reports=n',
        '--output-format=colorized',
        '-d',
        'C0103',
        '-d',
        'E0602',
    ]
    _assert_list_equals(expected, the_runner.args)
