#!/usr/bin/python3
"""
Module that contains the function number_of_lines
"""


def number_of_lines(filename=""):
    """ reads a text file and prints it to stdout """
    counter = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            counter += 1
    return counter
