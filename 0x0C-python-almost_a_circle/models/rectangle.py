#!/usr/bin/python3
"""
Module containing the class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ creates an instance of a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes the rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ method to get the area of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """ method to print a rectangle using the # character """
        string = ""
        if (self.__width != 0) or (self.__height != 0):
            for i in range(self.__y):
                string += "\n"
            for y in range(self.__height):
                for x in range(self.__x):
                    string += " "
                string += "#" * self.__width + "\n"
            string = string[:-1]
            print(string)

    def __str__(self):
        """ method to print the string represenation of a Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ method that assigns an argument to each attribute """
        length = len(args)
        if length > 0:
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.width = args[1]
            if length >= 3:
                self.height = args[2]
            if length >= 4:
                self.x = args[3]
            if length >= 5:
                self.y = args[4]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
