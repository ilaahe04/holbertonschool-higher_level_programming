#!/usr/bin/python3
"""Class Base"""
import json


class Base:
    """A class named base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Update the class Base"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
