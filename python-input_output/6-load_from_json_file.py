#!/usr/bin/python3
"""JSON"""


import json


def load_from_json_file(filename):
    """load from json"""
    with open(filename, mode="r") as f:
        json.load(f)
