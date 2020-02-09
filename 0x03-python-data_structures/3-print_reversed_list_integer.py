#!/usr/bin/python3
"""
Module containing the function print_reversed_list_integer
"""


def print_reversed_list_integer(my_list=[]):
    """ prints all integers of a list in reverse order """
    if my_list:  # if my_list exists
        for integer in my_list[::-1]:
            print("{:d}".format(integer))
