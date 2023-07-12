#!/usr/bin/python3
"""Define a text file line counting function."""


def write_file(filename="", text=""):
    """
    writes a string to file:

     Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
