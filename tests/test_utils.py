import pytest
from shortener.utils import generate_short_code
import string

@pytest.mark.short_url_generator
def test_generate_short_code_length():
    length = 6
    short_code = generate_short_code(length)
    assert len(short_code) == length, f"Expected length {length}, but got {len(short_code)}"

@pytest.mark.short_url_generator
def test_generate_short_code_characters():
    short_code = generate_short_code()
    valid_characters = set(string.ascii_letters + string.digits)
    assert all(char in valid_characters for char in short_code), "Short code contains invalid characters"
