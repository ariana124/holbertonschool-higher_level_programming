#!/usr/bin/python3
"""
Module that contains the function write_file
"""


def write_file(filename="", text=""):
    """ writes a string to a text file and returns the number of characters """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
