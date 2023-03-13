#!/usr/bin/python3
def no_c(my_string):
    for i in mystring:
        if i != 'c' and i != 'C':
            print("{}".format(i), end="")
    print()
