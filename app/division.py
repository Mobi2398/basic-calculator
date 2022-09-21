"""This file contains division function(s)"""


def division(value1, value2):
    """Returns the quotient of 2 values"""
    try:
        return value1 / value2
    except ZeroDivisionError:
        return "Cannot be divided by zero"
