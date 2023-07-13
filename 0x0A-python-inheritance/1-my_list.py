#!/usr/bin/python3
"""Define a class that inherits from list"""


class Mylist(list):
    """Implements sorted printing for the built-in list class."""
    
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
