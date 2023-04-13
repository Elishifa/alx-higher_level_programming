#!/usr/bin/python3

"""
Function checks an object if its the instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Returns true if object is exactly the instance otherwise false"""
    return (type(obj) == a_class)
