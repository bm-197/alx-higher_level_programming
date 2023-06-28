#!/usr/bin/python3

"""Define a square with size."""


class Square:
    """represent a square with size 'size'."""

    def __init__(self, size=0):
        """intialize square.

        Args:
            size (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """retrive size."""
        return (self.__size)

    @size.setter
    def size(self, size):
         if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns the area of the current."""
        return (self.__size ** 2)
