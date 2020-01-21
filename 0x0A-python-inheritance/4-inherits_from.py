#!/usr/bin/python3
"""
Module that contains the function inherits_from
"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class, otherwise False """
    return isinstance(type(obj), a_class) is not issubclass(type(obj), a_class)
