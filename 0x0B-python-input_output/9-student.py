#!/usr/bin/python3
"""Define a class student."""


class Student():
    """Represents a students."""

    def __init__(self, first_name, last_name, age):
        """initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance.
        """
        return self.__dict__
