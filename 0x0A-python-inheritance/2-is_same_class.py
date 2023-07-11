#!/usr/bin/python3
"""Define checker for if an object is Instance."""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly
    an instance of the specified class
    ; otherwise False.

    Args:
        obj (any): the object to be checked
        a_class (type): the class the object suppose to much

    Return:
        True if obj is a_class; otherwise False
    """

    if type(obj) == a_class:
        return True
    return False
