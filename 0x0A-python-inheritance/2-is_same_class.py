#!/usr/bin/python3

"""
Function checks an object if its the instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Return: 
              If object is exactly the instance = True
              otherwise = False
    """
    return (type(obj) == a_class)
