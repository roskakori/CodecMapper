"""
Setup for ebcdic package.

Developer cheat sheet
---------------------

Bump version number:

  1. Possibly update copyright year in:

     * ebcdic/__init__.py
     * LICENSE.txt and
     * README.rst

  2. Edit ebcdic/__init__.py:__version_info__.
  3. Describe changes in README.rst.

Upload release to PyPI::

  $ git checkout master
  $ git pull
  $ ant test
  $ cd ebcdic
  $ python setup.py bdist_wheel upload

Update production branch::

  $ git checkout production
  $ git merge master
  $ git push

Tag a release::

  $ git tag -a -m "Tagged version 1.x.x." v1.x.x
  $ git push --tags

"""
from __future__ import absolute_import

from setuptools import setup

import io
import os

import ebcdic

# Read the README text to use as long description.
_PACKAGE_FOLDER = os.path.dirname(__file__)
readme_path = os.path.join(_PACKAGE_FOLDER, 'README.rst')
with io.open(readme_path, 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='ebcdic',
    version=ebcdic.__version__,
    description='Additional EBCDIC codecs',
    long_description=long_description,
    url='https://pypi.python.org/pypi/ebcdic',
    author='Thomas Aglassinger',
    author_email='roskakori@users.sourceforge.net',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Text Processing',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='codec text unicode ebcdic',
    packages=['ebcdic'],
    test_suite='ebcdic.test.test_ebcdic',
)
