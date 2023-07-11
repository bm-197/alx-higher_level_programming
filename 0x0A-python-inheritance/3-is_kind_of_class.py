#!/usr/bin/python3
"""Define a fucntion to check same class or inherit from."""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, 
    or if the object is an instance of a class
    that inherited from, the specified class
    ; otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """

    if isinstance(obj, a_class):
        return True
    return False
