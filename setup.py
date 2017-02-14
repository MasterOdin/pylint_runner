"""
setup.py
"""

import os
from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as open_file:
        return open_file.read()


def get_requirements():
    """Get requirements from requirements.txt file"""
    install_reqs = parse_requirements("requirements.txt", session=PipSession())
    return [str(ir.req) for ir in install_reqs]


setup(
    name='pylint_runner',
    version='0.4.0',
    packages=['pylint_runner'],
    url='http://github.com/MasterOdin/pylint_runner',
    license='MIT',
    author='Matthew Peveler',
    author_email='matt.peveler@gmail.com',
    description='Run pylint recursively on all py files in current and sub directories',
    # long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read(),
    entry_points={
        'console_scripts': [
            'pylint_runner = pylint_runner.main:main',
        ]
    },
    install_requires=get_requirements(),
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 3 - Alpha',
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
        'Programming Language :: Python :: 3.5'
    ],
)
