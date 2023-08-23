import addition
import pytest

def test_add():
    assert addtion.add(1, 2) == 3
    assert addtion.add(1, 1) == 2
    assert addtion.add(1, 0) == 1
    assert addtion.add(1, -1) == 0
    assert addtion.add(1, -2) == -1
    assert addtion.add(1, -3) == -2 

def test_sub():
    assert addtion.sub(1, 2) == -1
    assert addtion.sub(1, 1) == 0
    assert addtion.sub(1, 0) == 1
    assert addtion.sub(1, -1) == 2
    assert addtion.sub(1, -2) == 3
    assert addtion.sub(1, -3) == 4
