#!/usr/bin/python3
#0-read_file.py
"""
   Defines the read_file function
"""


def read_file(filename=""):
    """reads and prints text file(UTF8) to
    standard output
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
