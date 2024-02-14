#!/usr/bin/python3

import unittest

from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
    def test_size_validation(self):
        with self.assertRaises(ValueError):
            Square(-5)
    def test_size_property(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
    if __name__ == '__main__':
        unittest.main()
