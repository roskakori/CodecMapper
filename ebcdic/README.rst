ebcdic
======

``ebcdic`` is a Python package adding additional EBCDIC codecs for data
exchange with legacy system. It works with Python 2.7 and Python 3.4+.

`EBCDIC <https://en.wikipedia.org/wiki/EBCDIC>`_ is short for Extended Binary
Coded Decimal Interchange Code and is a family of character encodings that is
mainly used on mainframe computers. There is no real point in using it unless
you have to exchange data with legacy systems that still only support EBCDIC
as character encoding.


Installation
------------

The ``ebcdic`` package is available from https://pypi.python.org/pypi/ebcdic
and can be installed using pip::

  pip install ebcdic


Example usage
-------------

To encode ``'hello world'`` on EBCDIC systems in German speaking countries,
use::

  >>> import ebcdic
  >>> 'hello world'.encode('cp1141')
  b'\x88\x85\x93\x93\x96@\xa6\x96\x99\x93\x84O'


Supported codecs
----------------

The ``ebcdic`` package includes EBCDIC codecs for the following regions:

* cp290 - Japan (Katakana)
* cp420 - Arabic bilingual
* cp424 - Israel (Hebrew)
* cp833 - Korea Extended (single byte)
* cp838 - Thailand
* cp870 - Eastern Europe (Poland, Hungary, Czech, Slovakia, Slovenia,
  Croatian, Serbia, Bulgarian); represents Latin-2
* cp1097 - Iran (Farsi)
* cp1140 - Australia, Brazil, Canada, New Zealand, Portugal, South Africa,
  USA
* cp1141 - Austria, Germany, Switzerland
* cp1142 - Denmark, Norway
* cp1143 - Finland, Sweden
* cp1144 - Italy
* cp1145 - Latin America, Spain
* cp1146 - Great Britain, Ireland, North Ireland
* cp1147 - France
* cp1148 - International
* cp1148ms - International, Microsoft interpretation; similar to cp1148
  except that 0x15 is mapped to 0x85 ("next line") instead if 0x0a
  ("linefeed")
* cp1149 - Iceland

It also includes legacy codecs:

* cp037 - Australia, Brazil, Canada, New Zealand, Portugal, South Africa;
  similar to cp1140 but without Euro sign
* cp273 - Austria, Germany, Switzerland; similar to cp1141 but without Euro
  sign
* cp277 - Denmark, Norway; similar to cp1142 but without Euro sign
* cp278 - Finland, Sweden; similar to cp1143 but without Euro sign
* cp280 - Italy; similar to cp1141 but without Euro sign
* cp284 - Latin America, Spain; similar to cp1145 but without Euro sign
* cp285 - Great Britain, Ireland, North Ireland; similar to cp1146 but
  without Euro sign
* cp297 - France; similar to cp1147 but without Euro sign
* cp500 - International; similar to cp1148 but without Euro sign
* cp500ms - International, Microsoft interpretation; identical to
  codecs.cp500 similar to ebcdic.cp500 except that 0x15 is mapped to 0x85
  ("next line") instead if 0x0a ("linefeed")
* cp871 - Iceland; similar to cp1149 but without Euro sign
* cp875 - Greece;  similar to cp9067 but without Euro sign and a few
  other characters
* cp1025 - Cyrillic
* cp1047 - Open Systems (MVS C compiler)
* cp1112 - Estonia, Latvia, Lithuania (Baltic)
* cp1122 - Estonia;  similar to cp1157 but without Euro sign
* cp1123 - Ukraine; similar to cp1158 but without Euro sign

Codecs in the standard library overrule some of these codecs. At the time of
this writing this concerns cp037, cp273 (since 3.4), cp500 and cp1140.

To see get a list of EBCDIC codecs that are already provided by different
sources, use ``ebcdic.ignored_codec_names()``. For example, with Python 3.6
the result is::

  >>> ebcdic.ignored_codec_names()
  ['cp037', 'cp1140', 'cp273', 'cp424', 'cp500', 'cp875']


Unsupported codecs
------------------

According to a
`comprehensive list of code pages <https://www.aivosto.com/articles/charsets-codepages.html>`_,
there are additional codecs this package does not support yet. Possible
reasons and solutions are:

1. It's a double byte codec, e.g. cp834 (Korea). Technically ``CodecMapper``
   can easily support them by increasing the mapping size from 256 to 65536.
   Due lack of test date and access to Asian mainframes this was deemed too
   experimental for now.
2. The codec contains combining characters, e.g. cp1132 (Lao) which allows
   to represent more than 256 characters combining several characters.
3. Java does not include a mapping for the respective code page, e.g.
   cp410/880 (Cyrillic). You can add such a codec based on the information
   found at the link above and submit an enhancement request for the Java
   standard library. Once it is released, simply add the new codec to
   the ``build.xml`` as described below.
4. I missed a codec. Simply open an issue on Github at
   https://github.com/roskakori/CodecMapper/issues and it will be added with
   the next version.


Source code
-----------

These codecs have been generated using CodecMapper, available from
https://github.com/roskakori/CodecMapper. Read the README in order to
to build the ebcdic package from source.

To add another 8 bit EBCDIC codec just extend the ant target ``ebcdic`` in
``build.xml`` using a line like::

   <arg value="cpXXX" />

Replace ``XXX`` by the number of the 8 bit code page you want to include.

Then run::

  ant test

to build and test the distribution.

The ``ebcdic/setup.py`` automatically includes the new encoding in the package
and ``ebcdic/__init__.py`` registers it during ``import ebcdic``, so no
further steps are needed.


Changes
-------

Version 1.1.1, 2019-08-09

* Moved license information from README to LICENSE (#5). This required the
  distribution to change from sdist to wheel because apparently it is a
  major challenge to include a text file in a platform independent way (#11).

  Sadly this breaks compatibility with Python 2.6, 3.1, 3.2 and 3.3. If you
  still need ``ebcdic`` with one of these Python versions, use
  ``ebcdic-1.0.0``.

  This took several attempts and intermediate releases that where broken in
  different ways on different platforms. To prevent people from accidentally
  installing one of these broken releases they have been removed from PyPI.
  If you still want to take a look at them, use the
  `respective tags <https://github.com/roskakori/CodecMapper/releases>`_.

Version 1.0.0, 2019-06-06

* Changed development status to "Production/Stable".
* Added international code pages cp500ms and cp1148ms which are the Microsoft
  interpretations of the respective IBM code pages. The only difference is
  that 0x1f is mapped to 0x85 ("next line") instead of 0x0a ("new line").
  Note that codecs.cp500 included with the Python standard library also uses
  the Microsoft interpretation (#4).
* Added Arabian bilingual code page 420.
* Added Baltic code page 1112.
* Added Cyrillic code page 1025.
* Added Eastern Europe code page 870.
* Added Estonian code pages 1122 and 1157.
* Added Greek code page 875.
* Added Farsi Bilingual code page 1097.
* Added Hebrew code page 424 and 803.
* Added Korean code page 833.
* Added Meahreb/French code page 425.
* Added Japanese (Katakana) code page 290.
* Added Thailand code page 838.
* Added Turkish code page 322.
* Added Ukraine code page 1123.
* Added Python 3.5 to 3.8 as supported version.
* Improved PEP8 conformance of generated codecs.


Version 0.7, 2014-11-17

* Clarified which codecs are already part of the standard library and that
  these codecs overrule the ``ebcdic`` package. Also added a function
  ``ebcdic.ignored_codec_names()`` that returns the name of the EBCDIC codecs
  provided by other means. To obtain access to ``ebcdic`` codecs overruled by
  the standard library, use ``ebcdic.lookup()``.
* Cleaned up (PEP8, __all__, typos, ...).


Version 0.6, 2014-11-15

* Added support for Python 2.6+ and 3.1+ (#1).
* Included a modified version of ``gencodec.py`` that still builds maps
  instead of tables so the generated codecs work with Python versions earlier
  than 3.3. It also does a `from __future__ import unicode_literals` so the
  codecs even work with Python 2.6+ using the same source code. As a side
  effect, this simplifies building the codecs because it removes the the need
  for a local copy of the cpython source code.


Version 0.5, 2014-11-13

* Initial public release
