#!/usr/bin/python3
"""Define a class for Rectangle inherits form Base geometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangele(BaseGeometry):
    """Represents a Rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize the rectangle.

        Args:
            width (int): the width of the rec
            height (int): the height of the rec
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
