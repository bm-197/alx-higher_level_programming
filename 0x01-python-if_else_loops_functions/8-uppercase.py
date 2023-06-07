#!/usr/bin/python3


def uppercase(str):
    """print a string in uppercase followed by a new line"""
    ascii_code = 0
    for char in str:
        ascii_code = ord(char)
        if ascii_code >= 97 and ascii_code < 123:
            print('{}'.format(chr(ascii_code - 32), end="")
        else:
            print('{}'.format(char), end="")

