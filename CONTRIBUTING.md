## Developer cheat sheet

Bump version number:

1. Possibly update copyright year in:

   - `ebcdic/__init__.py`
   - `LICENSE.txt` and
   - `README.rst`

2. Edit `ebcdic/_version.py:__version__`.
3. Describe changes in `README.rst`.

Upload release to PyPI::

```console
$ git checkout master
$ git pull
$ ant test
$ cd ebcdic
$ uv build
$ uv publish
```

Update production branch::

```console
$ git checkout production
$ git merge master
$ git push
```

Tag a release::

```console
$ git tag -a -m "Tagged version 1.x.x." v1.x.x
$ git push --tags
```
