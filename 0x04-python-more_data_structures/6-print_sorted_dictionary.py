#!/usr/bin/python3
"""
Module that contains the function print_sorted_dictionary
"""


def print_sorted_dictionary(a_dictionary):
    """ prints a dictionary by ordered keys """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
