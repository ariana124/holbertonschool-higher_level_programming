#!/usr/bin/python3
"""
Module containing the function no_c
"""


def no_c(my_string):
    """ removes all characters 'c' and 'C' from a string """
    new_string = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            new_string = new_string + letter
    return new_string
