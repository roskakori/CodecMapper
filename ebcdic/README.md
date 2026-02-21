# ebcdic

`ebcdic` is a Python package adding additional EBCDIC codecs for data exchange with legacy systems.

[EBCDIC](https://en.wikipedia.org/wiki/EBCDIC) is short for "Extended Binary Coded Decimal Interchange Code" and is a family of character encodings that is mainly used on mainframe computers. There is no real point in using it unless you have to exchange data with legacy systems.

This package requires Python 3.9 or later.

For compatibility with Python 2.7 to 3.3, use [version 1.1.1](https://pypi.org/project/ebcdic/1.1.1/).

For compatibility with Python 2.6 to 3.2, use [version 1.0.0](https://pypi.org/project/ebcdic/1.0.0/).

## Installation

The `ebcdic` package is available from <https://pypi.python.org/pypi/ebcdic> and can be installed using pip:

```console
pip install ebcdic
```

## Example usage

To encode `'hello world'` on EBCDIC systems in German-speaking countries, use:

```pycon
>>> import ebcdic
>>> 'hello world'.encode('cp1141')
b'\x88\x85\x93\x93\x96@\xa6\x96\x99\x93\x84O'
```

## Supported codecs

The `ebcdic` package includes EBCDIC codecs for the following regions:

- cp290 - Japan (Katakana)
- cp420 - Arabic bilingual
- cp424 - Israel (Hebrew)
- cp833 - Korea Extended (single byte)
- cp838 - Thailand
- cp870 - Eastern Europe (Poland, Hungary, Czech, Slovakia, Slovenia, Croatian, Serbia, Bulgarian); represents Latin-2
- cp1097 - Iran (Farsi)
- cp1140 - Australia, Brazil, Canada, New Zealand, Portugal, South Africa, USA
- cp1141 - Austria, Germany, Switzerland
- cp1142 - Denmark, Norway
- cp1143 - Finland, Sweden
- cp1144 - Italy
- cp1145 - Latin America, Spain
- cp1146 - Great Britain, Ireland, North Ireland
- cp1147 - France
- cp1148 - International
- cp1148ms - International, Microsoft interpretation; similar to cp1148 except that 0x15 is mapped to 0x85 ("next line") instead of 0x0a ("linefeed")
- cp1149 - Iceland

It also includes legacy codecs:

- cp037 - Australia, Brazil, Canada, New Zealand, Portugal, South Africa; similar to cp1140 but without Euro sign
- cp273 - Austria, Germany, Switzerland; similar to cp1141 but without Euro sign
- cp277 - Denmark, Norway; similar to cp1142 but without Euro sign
- cp278 - Finland, Sweden; similar to cp1143 but without Euro sign
- cp280 - Italy; similar to cp1141 but without Euro sign
- cp284 - Latin America, Spain; similar to cp1145 but without Euro sign
- cp285 - Great Britain, Ireland, North Ireland; similar to cp1146 but without Euro sign
- cp297 - France; similar to cp1147 but without Euro sign
- cp500 - International; similar to cp1148 but without Euro sign
- cp500ms - International, Microsoft interpretation; identical to codecs.cp500 similar to ebcdic.cp500 except that 0x15 is mapped to 0x85 ("next line") instead of 0x0a ("linefeed")
- cp871 - Iceland; similar to cp1149 but without Euro sign
- cp875 - Greece; similar to cp9067 but without Euro sign and a few other characters
- cp1025 - Cyrillic
- cp1047 - Open Systems (MVS C compiler)
- cp1112 - Estonia, Latvia, Lithuania (Baltic)
- cp1122 - Estonia; similar to cp1157 but without Euro sign
- cp1123 - Ukraine; similar to cp1158 but without Euro sign

Codecs in the standard library overrule some of these codecs. At the time of this writing this concerns cp037, cp273 (since 3.4), cp500 and cp1140.

To see get a list of EBCDIC codecs that are already provided by different sources, use `ebcdic.ignored_codec_names()`. For example, with Python 3.13 the result is:

```pycon
>>> ebcdic.ignored_codec_names()
['cp037', 'cp1140', 'cp273', 'cp424', 'cp500', 'cp875']
```

## Unsupported codecs

According to a [comprehensive list of code pages](https://www.aivosto.com/articles/charsets-codepages.html), there are additional codecs this package does not support yet. Possible reasons and solutions are:

1. It's a double byte codec e.g., cp834 (Korea). Technically `CodecMapper` can support them by increasing the mapping size from 256 to 65536. Due to lack of test data and access to Asian mainframes this was deemed too experimental for now.
2. The codec contains combining characters e.g., cp1132 (Lao) which allows representing more than 256 characters combining several characters.
3. Java does not include a mapping for the respective code page e.g., cp410/880 (Cyrillic). You can add such a codec based on the information found at the link above and submit an enhancement request for the Java standard library. Once it is released, add the new codec to the `build.xml` as described below.
4. I missed a codec. Open an issue on GitHub at <https://github.com/roskakori/CodecMapper/issues>, and it will be added with the next version.

## Source code

These codecs have been generated using CodecMapper, available from <https://github.com/roskakori/CodecMapper>. Read the [CONTRIBUTING.md](https://github.com/roskakori/CodecMapper/blob/master/CONTRIBUTING.md) to build the ebcdic package from the source and learn how to add more codecs.

## License

Copyright (c) 2013 - 2026, Thomas Aglassinger
All rights reserved.

Distributed under the BSD license, see [LICENSE.txt](https://github.com/roskakori/CodecMapper/blob/master/LICENSE.txt) for more information.
