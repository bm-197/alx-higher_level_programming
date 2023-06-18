#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value"""

    if a_dictionary:
        big_int = 0
        for k in a_dictionary.keys():
            if a_dictionary[k] > big_int:
                big_int = a_dictionary[k]
        return a_dictionary.keys()[a_dictionary.values().index(big_int)]
    else:
        return None
