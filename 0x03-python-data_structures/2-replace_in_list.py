#!/usr/bin/python3
"""
Module containing the function replace_in_list
"""


def replace_in_list(my_list, idx, element):
    """ returns an element of a list at a specific position """
    if (idx < 0) or (idx >= len(my_list)):
        return my_list
    my_list[idx] = element
    return my_list
