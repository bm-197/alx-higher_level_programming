#!/usr/bin/python3


def remove_char_at(str, n):
    """creates a copy of the string, removing the character at the position n"""
    for i in range(len(str)):
        if i != n:
            print('{}'.format(str[i]), end="")
