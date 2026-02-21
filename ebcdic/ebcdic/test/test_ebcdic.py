"""
Basic test for `ebcdic` package.
"""

import codecs

import pytest

import ebcdic


def test_has_codecs():
    assert len(ebcdic.codec_names) > 0
    assert "cp1141" in ebcdic.codec_names


def test_can_recode_hello_world():
    _test_can_recode("hello world", ebcdic.codec_names)


def _test_can_recode(text, codec_names):
    for codec_name in codec_names:
        encoded_text = text.encode(codec_name)
        recoded_text = encoded_text.decode(codec_name)
        assert text == recoded_text, f"{codec_name}: {text!r} != {recoded_text!r}"


def test_can_recode_euro_sign():
    _test_can_recode("\N{EURO SIGN}", ["cp1141", "cp1148", "cp1148ms"])


def test_has_ignored_codec_names():
    assert "cp500" in ebcdic.ignored_codec_names()


def test_can_lookup_ebcdic_codec():
    ebcdic_cp500 = ebcdic.lookup("cp500")
    standard_cp500 = codecs.lookup("cp500")
    assert ebcdic_cp500 != standard_cp500


def test_fails_on_lookup_of_unknown_ebcdic_codec():
    with pytest.raises(LookupError):
        ebcdic.lookup("cpNone")


def test_ignored_codecs_are_identical_to_standard_library():
    def encoded(code, codec):
        return chr(code).encode(codec.name, errors="replace")

    for codec_name in ebcdic.ignored_codec_names():
        ebcdic_codec = ebcdic.lookup(codec_name)
        assert ebcdic_codec is not None, codec_name
        standard_codec = codecs.lookup(codec_name)
        assert standard_codec is not None, codec_name
        for code in range(256):
            ebcdic_char = encoded(code, ebcdic_codec)
            standard_char = encoded(code, standard_codec)
            assert ebcdic_char == standard_char, f"{codec_name} at {code}: {ebcdic_char!r} != {standard_char!r}"
