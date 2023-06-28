#!/usr/bin/python3

"""Define a square with size."""


class Square:
    """Represent a square with size 'size'."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int): size of the new square.
        """
        self.size = size
        self.poistion = position

    @property
    def size(self):
        """retrive current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        """retrive the postion of the square."""
        return (self.__position)
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position == value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print("")
        else:
            for k in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ")
                for l in range(self.__size):
                    print("#")
                print("")
