#!/usr/bin/python3
"""Module to add"""


def add_integer(a, b=98):
    """Return the integer sum of a and b.

    Args:
        a (int): num 1
        b (int): num 2

    Raises:
        TypeError: if a or b are non-integer

    Returns:
        the sum of a and b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
