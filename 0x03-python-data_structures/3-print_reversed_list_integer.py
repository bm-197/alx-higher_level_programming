#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order."""

    for i in reversed(my_list):
            print("{:d}".format(i))
