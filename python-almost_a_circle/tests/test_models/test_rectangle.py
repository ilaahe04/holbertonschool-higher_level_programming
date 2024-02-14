#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        rect = Rectangle(10, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
    
    def test_width_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)
    
    def test_height_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -5)
    
    def test_x_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -1)
    
    def test_y_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 0, -1)

    def test_area(self):
        rect = Rectangle(10, 5)
        self.assertEqual(rect.area(), 50)

    def test_update_args(self):
        rect = Rectangle(10, 5, 0, 0, 1)
        rect.update(2, 20, 10, 1, 1)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 1)
    
    def test_update_kwargs(self):
        rect = Rectangle(10, 5, 0, 0, 1)
        rect.update(height=15, width=5, id=89, y=2, x=2)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 15)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 2)

    def test_to_dictionary(self):
        rect = Rectangle(10, 5, 1, 2, 3)
        rect_dict = rect.to_dictionary()
        expected = {'id': 3, 'width': 10, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(rect_dict, expected)
