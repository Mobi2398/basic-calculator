"""This is the starting test file"""
from app.addition import addition


def test_addition():
    """This always passes"""
    assert addition(2, 2) == 4
