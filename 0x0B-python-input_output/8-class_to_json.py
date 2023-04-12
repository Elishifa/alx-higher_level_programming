#!/usr/bin/python3

"""
   For JSON serialization this function defines
   a Python class-to-JSON function
"""


def class_to_json(obj):
    """This function returns dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    return obj.__dict__
