#!/usr/bin/python3
"""Class Square that inherits rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """set the side of square"""
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".\
               format(self.id, self.x, self.y, self.size)