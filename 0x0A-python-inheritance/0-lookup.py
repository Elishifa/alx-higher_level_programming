#!/usr/bin/python3
"""
    Function returns the list of 
    available attributes and methods of an object
"""


def lookup(obj):
    """This function returns a list of objects
    Args:
        obj (Any): object
    Returns:
        list: members and attributes list
    """
    return dir(obj)
