#!/usr/bin/python3

"""
Checking for an instance of an object
"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is an instance of specified class otherwise False"""
    return (isinstance(obj, a_class))
