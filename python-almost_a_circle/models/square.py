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

    def update(self, *args, **kwargs):
        """ Function"""
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        else:
            try:
                self.id = kwargs['id']
            except Exception:
                pass
            try:
                self.width = kwargs['size']
            except Exception:
                pass
            try:
                self.height = kwargs['size']
            except Exception:
                pass
            try:
                self.x = kwargs['x']
            except Exception:
                pass
            try:
                self.y = kwargs['y']
            except Exception:
                pass

    def to_dictionary(self):
        """Turn class atribute to dictionary"""
        dic = {"id": self.id,
               "size": self.size,
               "x": self.x,
               "y": self.y}
        return dic
