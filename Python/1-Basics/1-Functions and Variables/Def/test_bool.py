import pytest
from Bool import is_even

def test_bool():
    assert is_even(2) % 2 == 0

def test_bool():
    assert is_even(5) % 2 == 0

def test_bool():
    assert is_even(0) % 2 == 0

def test_bool():
    assert is_even(-2) % 2 == 0 

def test_bool():
    assert is_even(-3) % 2 == 0

def in_put():
    with pytest.raises(ValueError):
        is_even("Cat")