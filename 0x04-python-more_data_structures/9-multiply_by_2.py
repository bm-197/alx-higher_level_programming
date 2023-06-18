#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    a_dictionary.values() = list(map(lambda x: x * 2, a_dictionary.values()))
    return a_dictionary
