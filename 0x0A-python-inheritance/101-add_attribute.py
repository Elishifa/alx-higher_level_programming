#!/usr/bin/python3

"""
Adds a new attribute to the object
"""


def add_attribute(obj, name, value):
    """
        This function adds a new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
