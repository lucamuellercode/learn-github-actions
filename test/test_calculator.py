from src.calculator import add
from src.calculator import subtract
import pytest

def test_add():
    assert add(1,2) == 3
    assert add(-2,2) == 0
    assert add(0,0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5