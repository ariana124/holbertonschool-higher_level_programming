#!/usr/bin/python3
"""
Module containing the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ creates an instance of a Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes the Square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ method to print the string representation of a Square """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """ method that assigns an argument to each attribute """
        length = len(args)
        if length > 0:
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.size = args[1]
            if length >= 3:
                self.x = args[2]
            if length >= 4:
                self.y = args[3]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
