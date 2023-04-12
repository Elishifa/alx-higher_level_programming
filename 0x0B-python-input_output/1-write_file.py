#!/usr/bin/python3

"""
   Contains a file_writing function.
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Returns:
        Number of written characters.
    """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
