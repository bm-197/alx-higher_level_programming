#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None or my_list = []:
        return None
    
    max_num = 0
    for i in my_list:
        if i > max_num:
            max_num = i
    return max_num
