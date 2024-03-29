#!/usr/bin/python3

"""
   This fxn defines the class student.
"""


class Student:
    """Student representation."""

    def __init__(self, first_name, last_name, age):
        """Initializing the new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student
        instance
        """
        return self.__dict__
