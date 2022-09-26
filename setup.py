"""
setup.py
"""

import sys
from setuptools import setup
from pylint_runner import __author__, __version__

MAJOR_VERSION = sys.version_info[0]
MAJOR_MINOR_VERSION = ".".join([str(x) for x in sys.version_info[0:2]])


def get_requirements():
    """Get requirements from requirements.txt file"""
    with open("requirements.txt", encoding='ascii') as requirements:
        reqs = requirements.readlines()
    return reqs


CONSOLE_SCRIPTS = [
    "pylint_runner = pylint_runner.main:main",
    f"pylint_runner{MAJOR_VERSION} = pylint_runner.main:main",
    f"pylint_runner{MAJOR_MINOR_VERSION} = pylint_runner.main:main",
]

DESC = "Run pylint recursively on all py files in current and sub-directories"

with open('README.rst', encoding='utf-8') as readme:
    LONG_DESC = readme.read()

setup(
    name="pylint_runner",
    version=__version__,
    packages=["pylint_runner"],
    url="http://github.com/MasterOdin/pylint_runner",
    license="MIT",
    author=__author__,
    author_email="matt.peveler@gmail.com",
    description=DESC,
    long_description=LONG_DESC,
    entry_points={"console_scripts": CONSOLE_SCRIPTS},
    python_requires='>=3.5',
    install_requires=get_requirements(),
    tests_require=["pytest"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
)
