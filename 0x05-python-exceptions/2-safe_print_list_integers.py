#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    k = 0
    for i in range(x):
        try:
            k += 1
        except (ValueError, TypeError):
            break
    print("")
    return k
