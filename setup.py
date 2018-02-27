"""
setup.py
"""

import os
import sys
from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup
from pylint_runner import __author__, __version__

MAJOR_VERSION = sys.version_info[0]
MAJOR_MINOR_VERSION = '.'.join([str(x) for x in sys.version_info[0:2]])


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as open_file:
        return open_file.read()


def get_requirements():
    """Get requirements from requirements.txt file"""
    install_reqs = parse_requirements("requirements.txt", session=PipSession())
    return [str(ir.req) for ir in install_reqs]

CONSOLE_SCRIPTS = ['pylint_runner = pylint_runner.main:main',
                   'pylint_runner{0} = pylint_runner.main:main'.format(MAJOR_VERSION),
                   'pylint_runner{0} = pylint_runner.main:main'.format(MAJOR_MINOR_VERSION)]

setup(
    name='pylint_runner',
    version=__version__,
    packages=['pylint_runner'],
    url='http://github.com/MasterOdin/pylint_runner',
    license='MIT',
    author=__author__,
    author_email='matt.peveler@gmail.com',
    description='Run pylint recursively on all py files in current and sub directories',
    long_description=open('README.rst').read(),  # + '\n\n' + open('CHANGELOG.rst').read(),
    entry_points={"console_scripts": CONSOLE_SCRIPTS},
    install_requires=get_requirements(),
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)
