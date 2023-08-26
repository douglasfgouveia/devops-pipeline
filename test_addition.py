import addition
import pytest

def test_add():
    assert addition.add(1, 2) == 3
    assert addition.add(1, 1) == 2
    assert addition.add(1, 0) == 1
    assert addition.add(1, -1) == 0
    assert addition.add(1, -2) == -1
    assert addition.add(1, -3) == -2 

def test_sub():
    assert addition.sub(1, 2) == -1
    assert addition.sub(1, 1) == 0
    assert addition.sub(1, 0) == 1
    assert addition.sub(1, -1) == 2
    assert addition.sub(1, -2) == 3
    assert addition.sub(1, -3) == 4
