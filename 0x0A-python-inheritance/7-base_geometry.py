#!/usr/bin/python3
"""
Module containing the class BaseGeometry
"""


class BaseGeometry:
    def integer_validator(self, name, value):
        """ public instance method that validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """ public instance area method """
        raise Exception("area() is not implemented")
