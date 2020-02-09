#!/usr/bin/python3
"""
Module containing the function divisible_by_2
"""


def divisible_by_2(my_list=[]):
    """ returns a new list with True or False, depending on whether the integer
    at the same position in the original list is a multiple of 2 """
    new_list = []
    for number in my_list:
        if number % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
