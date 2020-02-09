#!/usr/bin/python3
"""
Module that contains the function multiply_by_2
"""


def multiply_by_2(a_dictionary):
    """ returns a new dictionary with all values multiplied by 2 """
    new_d = {}
    for key in a_dictionary:
        new_d[key] = a_dictionary[key] * 2
    return new_d
