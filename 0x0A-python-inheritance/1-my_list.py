#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
