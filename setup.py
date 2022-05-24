#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import codecs

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion


def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    try:
        f = codecs.open(os.path.join(here, *file_paths), 'r', 'latin1')
        version_file = f.read()
        f.close()
    except Exception:
        raise RuntimeError("Unable to find version string.")

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Get the long description from the relevant file
try:
    f = codecs.open('README.md', encoding='utf-8')
    long_description = f.read()
    f.close()
except Exception:
    long_description = ''


setup(
    name='backup',
    version=find_version('src/backup/__main__.py'),
    description='A tool for creating group files backups',
    long_description=long_description,
    author='d3vv3',
    author_email='devve.3@gmail.com',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Environment :: Console',
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="backup, group, folder, archive",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    # install_requires=[],
    entry_points={
        'console_scripts': [
            'backup = backup.__main__:main',
            'backup-cli=backup.__main__:main'
        ]
    })
