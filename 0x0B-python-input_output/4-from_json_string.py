#!/usr/bin/python3

"""
   Returns an object.
"""
import json


def from_json_string(my_str):
    """Returns the object (Python data structure in this case)
    represented by a JSON string
    """
    return json.loads(my_str)
