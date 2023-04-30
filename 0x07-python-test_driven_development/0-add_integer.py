#!/usr/bin/python3

"""
The module is composed by a funct that adds two numbers
"""


def add_integer(i, j=98):
    """ Function that adds two integer and/or float numbers
    Args:
        i: first number
        j: second number
    Returns:
        The addition of the two given numbers
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """

    if not isinstance(i, int) and not isinstance(i, float):
        raise TypeError("a must be an integer")
    if not isinstance(j, int) and not isinstance(j, float):
        raise TypeError("b must be an integer")
    i = int(i)
    j = int(j)
    return (i + j)
