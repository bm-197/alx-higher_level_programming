#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 and idx > (len(mylist) - 1):
        return(my_list)
    new_list = my_list[:]
    new_lsit[idx] = element
    return(new_list)
