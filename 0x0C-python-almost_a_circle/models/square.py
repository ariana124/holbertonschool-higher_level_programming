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
