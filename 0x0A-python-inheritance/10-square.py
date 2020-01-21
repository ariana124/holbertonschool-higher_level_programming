#!/usr/bin/python3
"""
Module containing the class Rectangle with properties from BaseGeometry
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """ initializes class Square """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ public instance area method """
        return self.__size ** 2

    def __str__(self):
        """ prints rectangle description """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
