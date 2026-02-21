# Contributing

This document describes how to work with the source code both for the generic CodecMapper and the Python ebcdic package.

## Getting the source code

To work with the source code, clone the repository:

```console
$ git clone https://github.com/roskakori/CodecMapper.git
```

## CodecMapper

### Requirements

To build and run CodecMapper, you need:

1. Java 1.7 or later
2. ant 1.8 or later, available from https://ant.apache.org/.

It might also work with earlier versions of ant, but this has not been tested.

### Usage

To build CodecMapper, run:

```console
$ ant dist
```

To generate a mapping file for a specific codec run, for example:

```console
$ java -jar dist/CodecMapper.jar iso-8859-15
```

The resulting mapping file is stored in `iso-8859-15.txt`. The generated mapping files are located in the same folder and have names like `iso-8859.15.mapping`.

## Python ebcdic package

As an example usage, CodecMapper includes the Python ebcdic package, which is located in the `ebcdic` folder. For general information about this package, take a look at the [ebcdic/README](ebcdic/README.md).

### Requirements

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

Then set up the pre-commit hooks that will lint the source code before a git commit:

```console
uv run pre-commit install
```

### Building and testing

To build the Python codecs and run the tests:

```console
$ ant test
```

After that, the build artifacts are located in `ebcdic/dist`.

## Adding more codecs

To add another 8-bit EBCDIC codec, extend the ant target `ebcdic` in `build.xml` using a line like:

```xml
<arg value="cpXXX" />
```

Replace `XXX` by the number of the 8-bit code page you want to include.

Then run:

```bash
ant test
```

to build and test the distribution.

## Adding a new release

Bump version number:

1. Possibly update copyright year in:

   - `ebcdic/__init__.py`,
   - `ebcdic/README.md`,
   - `LICENSE.txt`, and
   - `README.md`.

2. Edit `ebcdic/_version.py:__version__`.
3. Describe changes in `CHANGES.md`.

Upload a release to PyPI:

```console
$ git checkout master
$ git pull
$ ant test
$ cd ebcdic
$ rm -rf dist
$ uv build
$ uv publish
```

Update production branch:

```console
$ git checkout production
$ git merge master
$ git push
```

Tag a release:

```console
$ git tag --annotate --message "Tagged version 2.x.x." v2.x.x
$ git push --tags
```

Finally, add the [GitHub release](https://github.com/roskakori/CodecMapper/releases/new).
