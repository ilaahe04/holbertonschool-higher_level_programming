#!/usr/bin/python3
"""JSON"""


import json


def load_from_json_file(filename):
    """load from json"""
    with open(filename, mode="r") as f:
        obj = json.loads(f.read())
    return obj
