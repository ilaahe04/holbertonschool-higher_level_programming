#!/usr/bin/python3
"""Class Rectangle that inherits Base"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Find area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print rectangle with #"""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the class Rectangle"""
        arguments = ["id", "width", "height", "x", "y"]

        if args and len(args) != 0:
            for idx in range(len(args)):
                """setattr(self, arguments[idx], args[idx])"""
                if idx == 0:
                    self.id = args[idx]
                if idx == 1:
                    self.width = args[idx]
                if idx == 2:
                    self.height = args[idx]
                if idx == 3:
                    self.x = args[idx]
                if idx == 4:
                    self.y = args[idx]
        else:
            for i in kwargs:
                """settattr(self, key, value)"""
                if i == "id":
                    self.id = kwargs[i]
                if i == "width":
                    self.width = kwargs[i]
                if i == "height":
                    self.height = kwargs[i]
                if i == "x":
                    self.x = kwargs[i]
                if i == "y":
                    self.y = kwargs[i]

    def to_dictionary(self):
        """Turn class atribute to dictionary"""
        dic = {"id": self.id,
               "width": self.width,
               "height": self.height,
               "x": self.x,
               "y": self.y}
        return dic
