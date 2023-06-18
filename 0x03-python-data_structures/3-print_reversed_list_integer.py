#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order."""

    if isinstance(my_list, list):
        my_list.reverse()
        for i in range(len(my_list):
                print("{:d}".format(my_list[i]))
