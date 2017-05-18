"""
Basic test for `ebcdic` package.
"""


import codecs
import sys
import unittest

import ebcdic
import six

_IS_PYTHON2 = sys.version_info[0] == 2


class EbcdicTest(unittest.TestCase):
    """
    Test case of `ebcdic` package.
    """
    def test_has_codecs(self):
        self.assertTrue(len(ebcdic.codec_names) > 0)
        self.assertTrue('cp1141' in ebcdic.codec_names)

    def test_can_recode_hello_world(self):
        text = 'hello world'
        expected_encoded_text = b'\x88\x85\x93\x93\x96@\xa6\x96\x99\x93\x84'
        for codec_name in ebcdic.codec_names:
            encoded_text = text.encode(codec_name)
            self.assertEqual(expected_encoded_text, encoded_text,
                             '%s: %r != %r' % (codec_name, expected_encoded_text, encoded_text))
            recoded_text = encoded_text.decode(codec_name)
            self.assertEqual(text, recoded_text, '%s: %r != %r' % (codec_name, text, recoded_text))

    def test_has_ignored_codec_names(self):
        self.assertTrue('cp500' in ebcdic.ignored_codec_names())

    def test_can_lookup_ebcdic_codec(self):
        ebcdic_cp500 = ebcdic.lookup('cp500')
        standard_cp500 = codecs.lookup('cp500')
        self.assertNotEqual(ebcdic_cp500, standard_cp500)

    def test_fails_on_lookup_of_unknown_ebcdic_codec(self):
        self.assertRaises(LookupError, ebcdic.lookup, 'cpXXX')

    def test_ignored_codecs_are_identical_to_standard_library(self):
        def encoded(code, codec):
            if _IS_PYTHON2:
                result = six.text_type(chr(code), codec.name, errors='replace')
            else:
                result = chr(code).encode(codec.name, errors='replace')

        for codec_name in ebcdic.ignored_codec_names():
            ebcdic_codec = ebcdic.lookup(codec_name)
            self.assertNotEqual(ebcdic_codec, None, codec_name)
            standard_codec = codecs.lookup(codec_name)
            self.assertNotEqual(standard_codec, None, codec_name)
            for code in range(256):
                ebcdic_char = encoded(code, ebcdic_codec)
                standard_char = encoded(code, standard_codec)
                self.assertEqual(ebcdic_char, standard_char, '%s at %d: %r != %r'
                                 % (codec_name, code, ebcdic_char, standard_char))


if __name__ == '__main__':
    unittest.main()
