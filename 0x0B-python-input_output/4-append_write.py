#!/usr/bin/python3
"""
Module that contains the function append_write
"""


def append_write(filename="", text=""):
    """ appends a string to the end of a text file and returns the number
    of characters added """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
