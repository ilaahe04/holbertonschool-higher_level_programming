#!/usr/bin/python3

import unittest

from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_auto(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_manual(self):
        b2 = Base(42)
        self.assertEqual(b2.id, 42)

    def test_to_json_string_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_empty(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_empty(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])
