#!/usr/bin/python3
"""
   Creates an object
"""
import json


def load_from_json_file(filename):
    """This function creates an Object from
    a JSON file
    """
    with open(filename) as f:
        return json.load(f)
