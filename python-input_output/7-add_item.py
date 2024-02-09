#!/usr/bin/python3


"""
    The ``7. Load, add, save`` module
"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

try:
    txt = load_from_json_file("add_item.json")
except Exception:
    txt = []
save_to_json_file(txt + sys.argv[1:], "add_item.json")
