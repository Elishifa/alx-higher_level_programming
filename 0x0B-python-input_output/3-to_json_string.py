#!/usr/bin/python3
"""
   Returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """Function returns the JSON representation of an object
    (string in this case)
    """
    return json.dumps(my_obj)
