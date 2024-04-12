import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(5, -3) == 2
    assert add(-1, -1) == -2
    assert add(0, 0) == 0 

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(100, 50) == 50

def test_multiply():
    assert multiply(3, 7) == 21
    assert multiply(-1, 3) == -3
    assert multiply(0, 10) == 0
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(-1, 1) == -1
    assert divide(0, 1) == 0
    with pytest.raises(ValueError):
        divide(10, 0)
