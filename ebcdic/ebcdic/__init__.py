"""
EBCDIC codecs for data exchange with legacy systems.

For more information, visit <https://pypi.python.org/pypi/ebcdic/>.
"""
# Copyright (c) 2014, Thomas Aglassinger
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# 
# * Neither the name of Thomas Aglassinger nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from __future__ import absolute_import

__version_info__ = (0, 6, 0)
__version__ = '.'.join([str(item) for item in __version_info__])


def _codec_names():
    """
    Names of codecs included in the ebcdic package.
    """
    import glob
    import os.path

    package_folder = os.path.dirname(__file__)
    for codec_path in glob.glob(os.path.join(package_folder, 'cp*.py')):
        codec_name = os.path.splitext(os.path.basename(codec_path))[0]
        yield codec_name


def _register_codecs():
    """
    Register all codecs for which an 'cp*.py' can be found.
    """
    import codecs

    codec_name_to_info_map = {}
    for codec_name in codec_names:
        codec_module = __import__('ebcdic.' + codec_name, globals(), locals(), ['getregentry'])
        codec_name_to_info_map[codec_name] = codec_module.getregentry()
    codecs.register(lambda name: codec_name_to_info_map.get(name))


codec_names = sorted(_codec_names())
_register_codecs()