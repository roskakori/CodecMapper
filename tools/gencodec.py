"""Unicode Mapping Parser and Codec Generator.

This script parses Unicode mapping files as available from the Unicode
site (ftp://ftp.unicode.org/Public/MAPPINGS/) and creates Python codec
modules from them. The codecs use the standard character mapping codec
to actually apply the mapping.

Synopsis: gencodec.py dir codec_prefix

All files in dir are scanned and those producing non-empty mappings
will be written to <codec_prefix><mapname>.py with <mapname> being the
first part of the map's filename ('a' in a.b.c.txt) converted to
lowercase with hyphens replaced by underscores.

The tool also writes marshalled versions of the mapping tables to the
same location (with .mapping extension).

Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
(c) Copyright Guido van Rossum, 2000.

Table generation:
(c) Copyright Marc-Andre Lemburg, 2005.
    Licensed to PSF under a Contributor Agreement.

Modified by Thomas Aglassinger for improved PEP8 conformance of the
generated code.
"""

import codecs
import marshal
import os
import re

# Maximum allowed size of charmap tables
MAX_TABLE_SIZE = 8192

# Standard undefined Unicode code point
UNI_UNDEFINED = chr(0xFFFE)

# Placeholder for a missing codepoint
MISSING_CODE = -1

mapRE = re.compile(r'((?:0x[0-9a-fA-F]+\+?)+)'
                   r'\s+'
                   r'((?:(?:0x[0-9a-fA-Z]+|<[A-Za-z]+>)\+?)*)'
                   r'\s*'
                   r'(#.+)?')


def parsecodes(codes, len=len, range=range):
    """ Converts code combinations to either a single code integer
        or a tuple of integers.

        meta-codes (in angular brackets, e.g. <LR> and <RL>) are
        ignored.

        Empty codes or illegal ones are returned as None.

    """
    if not codes:
        return MISSING_CODE
    l = codes.split('+')
    if len(l) == 1:
        return int(l[0], 16)
    for i in range(len(l)):
        try:
            l[i] = int(l[i], 16)
        except ValueError:
            l[i] = MISSING_CODE
    l = [x for x in l if x != MISSING_CODE]
    if len(l) == 1:
        return l[0]
    else:
        return tuple(l)


def readmap(filename):
    with open(filename) as f:
        lines = f.readlines()
    enc2uni = {}
    identity = []
    unmapped = list(range(256))

    # UTC mapping tables per convention don't include the identity
    # mappings for code points 0x00 - 0x1F and 0x7F, unless these are
    # explicitly mapped to different characters or undefined
    for i in list(range(32)) + [127]:
        identity.append(i)
        unmapped.remove(i)
        enc2uni[i] = (i, 'CONTROL CHARACTER')

    for line in lines:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        m = mapRE.match(line)
        if not m:
            # print '* not matched: %s' % repr(line)
            continue
        enc, uni, comment = m.groups()
        enc = parsecodes(enc)
        uni = parsecodes(uni)
        comment = '' if comment is None else comment[1:].strip()
        if enc < 256:
            if enc in unmapped:
                unmapped.remove(enc)
            if enc == uni:
                identity.append(enc)
            enc2uni[enc] = (uni, comment)
        else:
            enc2uni[enc] = (uni, comment)

    # If there are more identity-mapped entries than unmapped entries,
    # it pays to generate an identity dictionary first, and add explicit
    # mappings to None for the rest
    if len(identity) >= len(unmapped):
        for enc in unmapped:
            enc2uni[enc] = (MISSING_CODE, "")
        enc2uni['IDENTITY'] = 256

    return enc2uni


def hexrepr(t, precision=4):
    if t is None:
        return 'None'
    try:
        len(t)
    except TypeError:
        return f'0x{t:0{precision}X}'
    try:
        return '(' + ', '.join([f'0x{item:0{precision}X}' for item in t]) + ')'
    except TypeError as why:
        print(f'* failed to convert {t!r}: {why}')
        raise


def python_mapdef_code(varname, map, comments=1, precisions=(2, 4)):
    l = []
    append = l.append
    if "IDENTITY" in map:
        append(f"{varname} = codecs.make_identity_dict(range({map['IDENTITY']}))")
        append(f"{varname}.update({{")
        splits = 1
        del map["IDENTITY"]
        identity = 1
    else:
        append(f"{varname} = {{")
        splits = 0
        identity = 0

    mappings = sorted(map.items())
    i = 0
    key_precision, value_precision = precisions
    for mapkey, mapvalue in mappings:
        mapcomment = ''
        if isinstance(mapkey, tuple):
            (mapkey, mapcomment) = mapkey
        if isinstance(mapvalue, tuple):
            (mapvalue, mapcomment) = mapvalue
        if mapkey is None:
            continue
        if (identity and
                mapkey == mapvalue and
                mapkey < 256):
            # No need to include identity mappings, since these
            # are already set for the first 256 code points.
            continue
        key = hexrepr(mapkey, key_precision)
        value = hexrepr(mapvalue, value_precision)
        if mapcomment and comments:
            append(f'    {key}: {value},\t#  {mapcomment}')
        else:
            append(f'    {key}: {value},')
        i += 1
        if i == 4096:
            # Split the definition into parts to that the Python
            # parser doesn't dump core
            if splits == 0:
                append('}')
            else:
                append('})')
            append(f'{varname}.update({{')
            i = 0
            splits = splits + 1
    if splits == 0:
        append('}')
    else:
        append('})')

    return l


def python_tabledef_code(varname, map, comments=1, key_precision=2):
    l = []
    append = l.append
    append(f'{varname} = (')

    # Analyze map and create table dict
    mappings = sorted(map.items())
    table = {}
    maxkey = 0
    if 'IDENTITY' in map:
        for key in range(256):
            table[key] = (key, '')
        maxkey = 255
        del map['IDENTITY']
    for mapkey, mapvalue in mappings:
        mapcomment = ''
        if isinstance(mapkey, tuple):
            (mapkey, mapcomment) = mapkey
        if isinstance(mapvalue, tuple):
            (mapvalue, mapcomment) = mapvalue
        if mapkey == MISSING_CODE:
            continue
        table[mapkey] = (mapvalue, mapcomment)
        if mapkey > maxkey:
            maxkey = mapkey
    if maxkey > MAX_TABLE_SIZE:
        # Table too large
        return None

    # Create table code
    for key in range(maxkey + 1):
        if key not in table:
            mapvalue = MISSING_CODE
            mapcomment = 'UNDEFINED'
        else:
            mapvalue, mapcomment = table[key]
        if mapvalue == MISSING_CODE:
            mapchar = UNI_UNDEFINED
        else:
            if isinstance(mapvalue, tuple):
                # 1-n mappings not supported
                return None
            else:
                mapchar = chr(mapvalue)
        if mapcomment and comments:
            mapchar_as_source = ascii(mapchar)
            append(f'    {mapchar_as_source} \t# {hexrepr(key, key_precision)} -> {mapcomment}')
        else:
            append(f'    {mapchar_as_source}')

    append(')')
    return l


def codegen(name, map, encodingname, comments=1):
    """ Returns Python source for the given map.

        Comments are included in the source, if comments is true (default).

    """
    # Generate code
    decoding_map_code = python_mapdef_code(
        'decoding_map',
        map,
        comments=comments)
    decoding_table_code = python_tabledef_code(
        'decoding_table',
        map,
        comments=comments)
    encoding_map_code = python_mapdef_code(
        'encoding_map',
        codecs.make_encoding_map(map),
        comments=comments,
        precisions=(4, 2))

    suffix = 'table' if decoding_table_code else 'map'

    l = [
        f'''""" 
Python Character Mapping Codec {encodingname} generated from '{name}' with gencodec.py.
"""

import codecs


# Codec APIs
class Codec(codecs.Codec):
    def encode(self, text, errors='strict'):
        return codecs.charmap_encode(text, errors, encoding_{suffix})

    def decode(self, data, errors='strict'):
        return codecs.charmap_decode(data, errors, decoding_{suffix})
''']
    l.append(f'''\

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, text, final=False):
        return codecs.charmap_encode(text, self.errors, encoding_{suffix})[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, data, final=False):
        return codecs.charmap_decode(data, self.errors, decoding_{suffix})[0]''')

    l.append('''

class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


# encodings module API
def getregentry():
    return codecs.CodecInfo(
        name={!r},
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )
'''.format(encodingname.replace('_', '-')))

    # Add decoding table or map (with preference to the table)
    if not decoding_table_code:
        l.append('''
# Decoding Map
''')
        l.extend(decoding_map_code)
    else:
        l.append('''
# Decoding Table
''')
        l.extend(decoding_table_code)

    # Add encoding map
    if decoding_table_code:
        l.append('''

# Encoding table
encoding_table = codecs.charmap_build(decoding_table)
''')
    else:
        l.append('''
# Encoding Map
''')
        l.extend(encoding_map_code)

    return '\n'.join(l).expandtabs()


def pymap(name, map, pyfile, encodingname, comments=1):
    code = codegen(name, map, encodingname, comments)
    with open(pyfile, 'w') as f:
        f.write(code)


def marshalmap(name, map, marshalfile):
    d = {}
    for e, (u, c) in map.items():
        d[e] = (u, c)
    with open(marshalfile, 'wb') as f:
        marshal.dump(d, f)


def convertdir(dir, dirprefix='', nameprefix='', comments=1):
    mapnames = os.listdir(dir)
    for mapname in mapnames:
        mappathname = os.path.join(dir, mapname)
        if not os.path.isfile(mappathname):
            continue
        name = os.path.split(mapname)[1]
        name = name.replace('-', '_')
        name = name.split('.')[0]
        name = name.lower()
        name = nameprefix + name
        codefile = name + '.py'
        marshalfile = name + '.mapping'
        print(f'converting {mapname} to {dirprefix + codefile} and {dirprefix + marshalfile}')
        try:
            map = readmap(os.path.join(dir, mapname))
            if not map:
                print('* map is empty; skipping')
            else:
                pymap(mappathname, map, dirprefix + codefile, name, comments)
                marshalmap(mappathname, map, dirprefix + marshalfile)
        except ValueError as why:
            print(f'* conversion failed: {why}')
            raise


def rewritepythondir(dir, dirprefix='', comments=1):
    mapnames = os.listdir(dir)
    for mapname in mapnames:
        if not mapname.endswith('.mapping'):
            continue
        name = mapname[:-len('.mapping')]
        codefile = name + '.py'
        print(f'converting {mapname} to {dirprefix + codefile}')
        try:
            with open(os.path.join(dir, mapname), 'rb') as f:
                map = marshal.load(f)
            if not map:
                print('* map is empty; skipping')
            else:
                pymap(mapname, map, dirprefix + codefile, name, comments)
        except ValueError as why:
            print(f'* conversion failed: {why}')


if __name__ == '__main__':

    import sys

    if 1:
        convertdir(*sys.argv[1:])
    else:
        rewritepythondir(*sys.argv[1:])
