# Changes

## Version 2.0.0, 2026-02-25

This is a pure technical release that does not change the functionality of the package.

It ensures that the package builds with a modern Python toolchain and continuous integration systems. For details, see [#8](https://github.com/roskakori/CodecMapper/issues/8), contributed by [Branch Vincent](https://github.com/branchv)). In addition, it cleans up some source files missing from the distribution (see [#17](https://github.com/roskakori/CodecMapper/issues/17)) and several minor issues in the documentation.

Because of this, support for Python 2 and Python 3.8 or older had to be dropped. If you are stuck with such a version, use [ebcdic 1.1.1](https://pypi.org/project/ebcdic/1.1.1/), which currently has the same functionality.

In addition, the documentation has been cleaned up to better conform to the standard layout of modern open source projects (see [#25](https://github.com/roskakori/CodecMapper/issues/25):

- The list of changes is now a separate `CHANGES.md` instead of part of the `ebcdic/README.md`.
- The `CONTRIBUTING.md` now includes all the instructions to build the package and run tests. Before, they were spreadout across the different `README` files.
- The main `README.md` is a concise overview pointing to the other parts of the documentation for details.

And finally, you can now show your appreciation of this package by [donating to it](https://roskakori.at/donate/donate-python-ebcdic/).

## Version 1.1.1, 2019-08-09

- Moved license information from README to LICENSE (#5). This required the distribution to change from sdist to wheel because apparently it is a major challenge to include a text file in a platform independent way (#11).

  Sadly this breaks compatibility with Python 2.6, 3.1, 3.2 and 3.3. If you still need `ebcdic` with one of these Python versions, use `ebcdic-1.0.0`.

  This took several attempts and intermediate releases that where broken in different ways on different platforms. To prevent people from accidentally installing one of these broken releases they have been removed from PyPI. If you still want to take a look at them, use the [respective tags](https://github.com/roskakori/CodecMapper/releases).

## Version 1.0.0, 2019-06-06

- Changed development status to "Production/Stable".
- Added international code pages cp500ms and cp1148ms which are the Microsoft interpretations of the respective IBM code pages. The only difference is that 0x1f is mapped to 0x85 ("next line") instead of 0x0a ("new line"). Note that codecs.cp500 included with the Python standard library also uses the Microsoft interpretation (#4).
- Added Arabian bilingual code page 420.
- Added Baltic code page 1112.
- Added Cyrillic code page 1025.
- Added Eastern Europe code page 870.
- Added Estonian code pages 1122 and 1157.
- Added Greek code page 875.
- Added Farsi Bilingual code page 1097.
- Added Hebrew code page 424 and 803.
- Added Korean code page 833.
- Added Meahreb/French code page 425.
- Added Japanese (Katakana) code page 290.
- Added Thailand code page 838.
- Added Turkish code page 322.
- Added Ukraine code page 1123.
- Added Python 3.5 to 3.8 as supported versions.
- Improved PEP8 conformance of generated codecs.

## Version 0.7, 2014-11-17

- Clarified which codecs are already part of the standard library and that these codecs overrule the `ebcdic` package. Also added a function `ebcdic.ignored_codec_names()` that returns the name of the EBCDIC codecs provided by other means. To obtain access to `ebcdic` codecs overruled by the standard library, use `ebcdic.lookup()`.
- Cleaned up (PEP8, `__all__`, typos, ...).

## Version 0.6, 2014-11-15

- Added support for Python 2.6+ and 3.1+ (#1).
- Included a modified version of `gencodec.py` that still builds maps instead of tables so the generated codecs work with Python versions earlier than 3.3. It also does a `from __future__ import unicode_literals` so the codecs even work with Python 2.6+ using the same source code. As a side effect, this simplifies building the codecs because it removes the the need for a local copy of the cpython source code.

## Version 0.5, 2014-11-13

- Initial public release
