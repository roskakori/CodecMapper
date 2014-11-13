"""
Basic test for ebcdic package.
"""
from __future__ import absolute_import

import unittest

import ebcdic

class EbcdicTest(unittest.TestCase):
    def test_has_codecs(self):
        self.assertTrue(len(ebcdic.codec_names) > 0)
        self.assertTrue('cp1141' in ebcdic.codec_names)


    def test_can_recode_hello_world(self):
        text = 'hello world'
        encoded_text = text.encode('cp1141')
        self.assertEqual(b'\x88\x85\x93\x93\x96@\xa6\x96\x99\x93\x84', encoded_text)
        recoded_text = encoded_text.decode('cp1141')
        self.assertEqual(text, recoded_text)


if __name__ == '__main__':
    unittest.main()
