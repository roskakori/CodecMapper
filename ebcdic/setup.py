"""
Setup for ebcdic package.

Developer cheat sheet
---------------------

Upload release to PyPI::

  $ ant test
  $ cd ebcdic
  $ python setup.py sdist --formats=zip upload

Tag a release::

  $ git tag -a -m "Tagged version 1.x." v1.x
  $ git push --tags

"""
from __future__ import absolute_import

from setuptools import setup

import io
import os

import ebcdic

# Read the README text to use as long description.
_package_folder = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(_package_folder, 'README.rst')
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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='codec text unicode ebcdic',
    packages=['ebcdic'],
    test_suite='ebcdic.test.test_ebcdic'
)
