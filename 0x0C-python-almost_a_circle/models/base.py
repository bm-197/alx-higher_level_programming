#!/usr/bin/python3
"""Define a base class."""


class Base:
    """Represents a base model.

    Attributes:
            __nb_objects (int): The number of intantiated.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base.

        Args:
            id (int): The identity of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
