#!/usr/bin/python3
"""Define a text file line counting function."""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and
    returns the number of characters written.
    """
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
        return lines
