"""
Setup for ebcdic package.
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
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing',
        'License :: OSI Approved :: BSD License',
        # TODO #1: 'Programming Language :: Python :: 2',
        # TODO #1: 'Programming Language :: Python :: 2.6',
        # TODO #1: 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='codec text unicode ebcdic',
    packages=['ebcdic'],
    test_suite = 'ebcdic.test.test_ebcdic'
)
