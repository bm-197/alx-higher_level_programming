#!/usr/bin/python3

def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    size = len(list_of_integers)
    l = list_of_integers
    pick = 0
    for i in range(size):
        if i != 0 or i != size:
            if l[i] > l[i - 1] and l[i + 1]:
                pick = l[i]

    return pick
