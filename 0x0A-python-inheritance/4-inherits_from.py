#!/usr/bin/python3

"""Checks a class instance"""


def inherits_from(obj, a_class):
    """Returns true if object is true otherwise false"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
