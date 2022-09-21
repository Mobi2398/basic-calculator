"""This is the starting test file"""
from app.division import division


def test_division():
    """This always passes"""
    assert division(4, 0) == "Cannot be divided by zero"

