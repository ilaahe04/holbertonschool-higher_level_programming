#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
import os

class TestRectangle(unittest.TestCase):

    def setUp(self):
        """Instances for rectangle"""
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(1, 2, 3)
        self.r3 = Rectangle(7, 7, 7, 7)
        self.r4 = Rectangle(1, 2, 3, 64, 5)
        self.new_dicts = {"id": 2, "width": 2, "height": 2, "x": 2, "y": 2}
        self.list_r1 = [self.r1]

    def test_checker(self):
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r3.y, 7)
        self.assertEqual(self.r4.id, 5)

        """Type Error"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

        """Value Error"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
      
    """Testing area"""
    def test_area(self):
        self.assertEqual(self.r1.area(), 2)

    """Testing __str__"""
    def test_str(self):
        self.assertEqual(self.r4.__str__(), "[Rectangle] (5) 3/64 - 1/2")

    def test_display(self):
        output = "#\n#\n"
        with patch("sys.stdout", new=StringIO()) as o:
            self.r1.display()
            self.assertEqual(o.getvalue(), output)
        output = "   #\n   #\n"
        with patch("sys.stdout", new=StringIO()) as o:
            self.r2.display()
            self.assertEqual(o.getvalue(), output)

    def test_dictionary(self):
        self.assertEqual(self.r4.to_dictionary(), {"width": 1, "height": 2, "x": 3, "y": 64, "id": 5})

    def test_update(self):
        self.r4.update(2, 4, 7, 8, 9)
        self.assertEqual(str(self.r4), "[Rectangle] (2) 8/9 - 4/7")

    def test_create(self):
        new = Rectangle.create(**self.new_dicts)
        self.assertEqual(str(new), "[Rectangle] (2) 2/2 - 2/2")

    def test_save_to_file_case_1(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
    
    def test_save_to_file2(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file3(self):
        Rectangle.save_to_file([Rectangle(1, 2, id=1)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')
    
    def test_load_from(self):
        self.assertEqual(Rectangle.load_from_file(), [])
    
        Rectangle.save_to_file(self.list_r1)
        self.assertEqual(self.list_r1[0].__str__(), Rectangle.load_from_file()[0].__str__())

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass 
