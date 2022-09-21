"""This is the starting test file"""
from app.multiplication import multiplication


def test_multiplication():
    """This always passes"""
    assert multiplication(2, 2) == 4
