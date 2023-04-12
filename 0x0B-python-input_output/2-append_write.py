#!/usr/bin/python3
"""
   Function that appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file
    Returns:
        Total added characters.
    """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
