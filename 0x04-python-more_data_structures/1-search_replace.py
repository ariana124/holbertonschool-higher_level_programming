#!/usr/bin/python3
"""
Module that contains the function search_replace
"""


def search_replace(my_list, search, replace):
    """ replaces all occurences of an element by another """
    return ([elem if elem is not search else replace for elem in my_list])
