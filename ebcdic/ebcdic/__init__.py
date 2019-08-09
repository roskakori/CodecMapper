"""
EBCDIC codecs for data exchange with legacy systems.

For more information, visit <https://pypi.python.org/pypi/ebcdic/>.
"""
# Copyright (c) 2013 - 2019, Thomas Aglassinger
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
from __future__ import absolute_import
import codecs


__all__ = [
    'codec_names',
    'ignored_codec_names',
    'lookup',
    '__version__',
    '__version_info__'
]
__version_info__ = (1, 1, 1)
__version__ = '.'.join([str(item) for item in __version_info__])


def _codec_names():
    """
    Names of the codecs included in the ebcdic package.
    """
    import glob
    import os.path

    package_folder = os.path.dirname(__file__)
    for codec_path in glob.glob(os.path.join(package_folder, 'cp*.py')):
        codec_name = os.path.splitext(os.path.basename(codec_path))[0]
        yield codec_name


def _create_codec_name_to_info_map():
    result = {}
    for codec_name in codec_names:
        codec_module = __import__('ebcdic.' + codec_name, globals(), locals(), ['getregentry'])
        result[codec_name] = codec_module.getregentry()
    return result


def _find_ebcdic_codec(code_name):
    """
    The `codec.CodecInfo` matching `codec_name` provided it is part of the
    package, otherwise `None`.
    """
    return _codec_name_to_info_map.get(code_name)


def ignored_codec_names():
    """
    A list of codec names in this package that are ignored because they are
    already provided by other means, e.g. the standard library.
    """
    return [codec_name
            for codec_name, codec_info in sorted(_codec_name_to_info_map.items())
            if codec_info != codecs.lookup(codec_name)
    ]


def lookup(codec_name):
    """
    The `codecs.CodecInfo` for the EBCDIC codec `codec_name`. An unknown
    `codecs_name` raises a `LookupError`.
    """
    result = _find_ebcdic_codec(codec_name)
    if result is None:
        raise LookupError('EBCDIC codec is %r but must be one of: %s' % (codec_name, codec_names))
    return result


# Names of the codecs included in the ebcdic package.
codec_names = sorted(_codec_names())
_codec_name_to_info_map = _create_codec_name_to_info_map()
codecs.register(_find_ebcdic_codec)
