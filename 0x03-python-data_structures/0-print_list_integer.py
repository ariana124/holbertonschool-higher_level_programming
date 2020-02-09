#!/usr/bin/python3
"""
Module containing the function print_list_integer
"""


def print_list_integer(my_list=[]):
    """ prints all integers of a list """
    for integer in my_list:
        print("{:d}".format(integer))
