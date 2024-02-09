#!/usr/bin/python3
"""json"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        j_dict = {}

        for attr, self in self.__dict__.items():
            if isinstance(self, (list, dict, str, int, bool)):
                j_dict[attr] = self

        return j_dict
