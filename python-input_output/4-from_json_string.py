#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def from_json_string(my_str):
    """Return the JSON representation of a string object."""
    return json.loads(my_str)
