#!/usr/bin/python3
"""json"""


def class_to_json(obj):
    """Initialize an empty dictionary"""
    j_dict = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            j_dict[attr] = value

    return j_dict
