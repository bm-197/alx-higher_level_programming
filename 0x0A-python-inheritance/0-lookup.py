#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    return a list of available attributes and methods of an object.
    """

    return (dir(obj))
