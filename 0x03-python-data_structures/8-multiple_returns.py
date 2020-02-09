#!/usr/bin/python3
"""
Module containing the function multiple_returns
"""


def multiple_returns(sentence):
    """ returns a tuple with the length of a string and its first character """
    length = len(sentence)
    if length == 0:
        firstchar = None
    else:
        firstchar = sentence[0]
    return(length, firstchar)
