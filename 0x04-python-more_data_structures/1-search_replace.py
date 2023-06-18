#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replaces all occurrences of 
    an element by another in a new list"""

    for i in range(len(my_list)):
        if my_list[i] == search:
            replace.append(search)
        else:
            replace.append(my_list[i])
