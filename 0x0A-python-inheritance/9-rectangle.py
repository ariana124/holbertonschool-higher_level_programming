#!/usr/bin/python3
"""
Module containing the class Rectangle with properties from BaseGeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """ initializes class Rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ public instance area method """
        return self.__width * self.__height

    def __str__(self):
        """ prints rectangle description """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
