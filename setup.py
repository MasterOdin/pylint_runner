"""
setup.py
"""

from setuptools import setup
import os


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as open_file:
        return open_file.read()

setup(
    name='pylint_runner',
    version='0.3',
    packages=['pylint_runner'],
    url='http://github.com/MasterOdin/pylint_runner',
    license='MIT',
    author='Matthew Peveler',
    author_email='matt.peveler@gmail.com',
    description='Run pylint recursively on all py files in current and sub directories',
    # long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read(),
    entry_points={
        'console_scripts': [
            'pylint_runner = pylint_runner.main:runner',
        ]
    },
    install_requires=['colorama', 'pylint'],
    tests_require=['nose'],
    #cmdclass={'test': nosetests},
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
        'Programming Language :: Python :: 3.4'
    ],
)
