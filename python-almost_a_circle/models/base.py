#!/usr/bin/python3
"""Class Base"""
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dicts))
        f.close()

    @staticmethod
    def from_json_string(json_string):
        """Function that returns the list"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        list_dicts = []
        try:
            with open("{}.json".format(cls.__name__),
                      "r") as f:
                read_data = f.read()
                list_json = cls.from_json_string(read_data)
                try:
                    for dictionary in list_json:
                        list_dicts.append(cls.create(**dictionary))
                except Exception:
                    pass
            f.close()
        except Exception:
            pass
        finally:
            return list_dicts
