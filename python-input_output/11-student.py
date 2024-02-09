#!/usr/bin/python3
"""json"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new = {}
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            for i in attrs:
                try:
                    new[i] = self.__dict__[i]
                except KeyError:
                    pass
            return new
        return self.__dict__

    def reload_from_json(self, json):
        try:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
        except KeyError:
            pass
