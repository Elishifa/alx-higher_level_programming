#!/usr/bin/python3

"""
   Defines read_file function
"""


def read_file(filename=""):
    """reads and prints text file to
    standard output
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
