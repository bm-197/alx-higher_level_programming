#!/usr/bin/python3

def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    size = len(list_of_integers)
    peak = 0
    if list_of_integers:
        return None
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers)
    for i in range(size):
        if i != 0 or i != size:
            if list_of_integers[i] > list_of_integers[i - 1] and list_of_integers[i + 1]:
                peak = l[i]

    return peak
