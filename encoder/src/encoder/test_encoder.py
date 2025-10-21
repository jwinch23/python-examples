import pytest
from encoder import run_length_encode

def test_basic_encoding():
    assert run_length_encode("aaabbc") == "a3b2c1"

def test_empty_string():
    assert run_length_encode("") == ""

def test_single_character():
    assert run_length_encode("a") == "a1"

def test_no_repeats():
    assert run_length_encode("abc") == "a1b1c1"

def test_long_repeats():
    assert run_length_encode("aaaaabbbbccdddddd") == "a5b4c2d6"

def test_whitespace_only():
    assert run_length_encode("   ") == " 3"

def test_special_characters():
    assert run_length_encode("$$$%%%") == "$3%3"

def test_invalid_input():
    with pytest.raises(TypeError):
        run_length_encode(123)