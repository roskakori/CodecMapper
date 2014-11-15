ebcdic
======

Ebcdic is a Python package adding additional EBCDIC encodings for data
exchange with legacy system. It works with Python 2.6+ and Python 3.2+.


Installation
------------

Ebcdic is available from https://pypi.python.org/pypi/ebcdic and can be
installed using pip::

  pip install ebcdic


Example usage
-------------

>>> import ebcdic
>>> 'hello world'.encode('cp1141')
b'\x88\x85\x93\x93\x96@\xa6\x96\x99\x93\x84O'


Supported codecs
----------------

Python already ships with the following EBCDIC codec:

* cp500 - international (without Euro sign)

The `ebcdic` package currently adds:

* cp1140 - Australia, Brazil, Canada, New Zealand, Portugal, South Africa,
  USA
* cp1141 - Germany, Austria
* cp1142 - Denmark, Norway
* cp1143 - Finland, Sweden
* cp1144 - Italy
* cp1145 - Latin America, Spain
* cp1146 - Great Britain, Ireland, North Ireland
* cp1147 - France
* cp1148 - international
* cp1149 - Iceland

It also adds legacy codecs that do not include the Euro sign:

* cp037 - similar to cp1140
* cp273 - similar to cp1141
* cp277 - similar to cp1142
* cp278 - similar to cp1143
* cp280 - similar to cp1144
* cp284 - similar to cp1145
* cp285 - similar to cp1146
* cp297 - similar to cp1147
* cp871 - similar to cp1149
* cp1047 - Open Systems (MVS C compiler)


Source code
-----------

These codecs have been generated using CodecMapper available from
https://github.com/roskakori/CodecMapper. Read the README in order to
to build the ebcdic package from source.

To add another 8 bit EBCDIC codec just extend the ant target `ebcdic` in
`build.xml` using a  line like::

   <arg value="cpXXX" />


License
-------

Copyright (c) 2014, Thomas Aglassinger
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

Changes
-------

Version 0.6, 2014-11-15
* Added support for Python 2.6+ and 3.1+ (#1).
* Included a modified version of `gencodec.py` that still builds maps instead
  of tables so the generated codecs work with Python version earlier than 3.3.
  It also does a `from __future__ import unicode_literals` so the codecs even
  work with Python 2.6+ using the same source code. As a side effect, this
  simplifies building the codecs because it removes the the need for a local
  copy of the cpython source code.

Version 0.5, 2014-11-13
* Initial public release
