#!/usr/bin/python3

def no_c(my_string):
    """removes all characters c and C from a string."""

    new_string = ""
    for string in my_string:
        if string != 'c' and string != 'C':
            new_string+=string

    return (new_string)
