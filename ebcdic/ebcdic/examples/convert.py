"""
Convert all "*.txt" files in a folder from EBCDIC cp1141 to UTF-8.
"""
from __future__ import print_function
from __future__ import unicode_literals

import glob
import os.path
import tempfile

# Register EBCDIC codecs.
import ebcdic  # noqa


if __name__ == '__main__':
    source_encoding = 'cp1141'
    target_encoding = 'utf-8'
    print('convert from %s to %s:' % (source_encoding, target_encoding))
    for source_path in glob.glob('*.txt'):
        target_name = os.path.splitext(os.path.basename(source_path))[0] + '_utf-8.txt'
        target_path = os.path.join(tempfile.tempdir(), target_name)
        print('  %s --> %s' % (source_path, target_path))
