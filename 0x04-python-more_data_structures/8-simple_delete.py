#!/usr/bin/python3
"""
Module that contains the function simple_delete
"""


def simple_delete(a_dictionary, key=""):
    """ deletes a key in a dictionary """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
