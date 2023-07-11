#!/usr/bin/python3
"""Define a class that inherits from list"""


class Mylist(list):
    """carry out a sorting method"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
