#!/usr/bin/python3
"""
Module that contains the function best_score
"""


def best_score(a_dictionary):
    """ returns a key with the biggest integer value """
    for key in a_dictionary:
        if key is None:
            return None
        else:
            max_val = max(a_dictionary)
            return max_val
