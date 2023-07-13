#!/usr/bin/python3
"""Define a class student."""


class Student():
    """Represents a students."""

    def __init__(self, first_name, last_name, age):
        """initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the student instance."""
        for k, v in json.items():
            setattr(self, k, v)
