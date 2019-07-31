CodecMapper
===========

CodecMapper derives mapping files from Java Charsets which can be processed
by Python's gencodec.py.


Requirements
------------

To build and run CodecMapper, you need:

  1. Java 1.7 or later
  2. ant 1.8 or later, available from https://ant.apache.org/.

It might also work with earlier versions of ant but this has not been tested.


Usage
-----

To build CodecMapper, run:

```sh
$ ant dist
```

To generate a mapping file for a specific codec, run for example:

```sh
$ java -jar dist/CodecMapper.jar iso-8859-15
```

The resulting mapping file is stored in `iso-8859-15.txt`. The generated mapping files
are located in the same folder and have names like
`iso-8859.15.mapping`.


EBCDIC codecs for Python
------------------------

As an example usage, CodecMapper can provide additional EBCDIC codecs for
Python, which can easily be packaged and distributed.

To test the Python codecs you need to setup a Pythen venv:

```sh
$ python -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install pycodestyle
```

After that you can build the Python codecs and run the tests:

```sh
$ ant test
```
For more information, browse the "ebcdic" folder of this distribution and
take a look at the README.rst.


Source code
-----------

See https://github.com/roskakori/CodecMapper.


License
-------

Copyright (c) 2013 - 2019, Thomas Aglassinger
All rights reserved.

Distributed under the BSD license, see [LICENSE.txt](LICENSE.txt) for more
information.