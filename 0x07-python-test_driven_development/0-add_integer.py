#!/usr/bin/python3
"""
Module add-integer
Definr a function that adds two integers
"""

def add_integer(a, b=98):
    """
    Return the addition of a and b,
    and raise an error if a and b are not integersor floats
    """
    if not isinstance(a, int) and not isinstance float(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance float(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
