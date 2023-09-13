#!/usr/bin/python3
"""Define a writing file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
    
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Return:
        the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
