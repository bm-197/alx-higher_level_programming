#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific position 
    without modifying the original list (like in C)."""

    if idx < 0 or idx >= len(index):
        return my_list
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
