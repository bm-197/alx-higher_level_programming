#!/usr/bin/python3
"""Define a Square class inheriting from Rectangle."""
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square."""

    def __init__(self, size):
        """Intialize the square.

        Args:
            size (int): the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """The area of the square."""
        return (self.__size ** 2)
