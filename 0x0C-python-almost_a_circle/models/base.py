#!/usr/bin/python3
"""Define a Base class."""


class Base():
    """Represents a Base class.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.

    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """initialize the base class.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = __nb_object
