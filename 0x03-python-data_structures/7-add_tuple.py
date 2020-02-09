#!/usr/bin/python3
"""
Module that contains the function add_tuple
"""


def add_tuple(tuple_a=(), tuple_b=()):
    """ returns the sum of 2 tuples """
    if len(tuple_a) < 1:
        a1 = 0
    else:
        a1 = tuple_a[0]

    if len(tuple_b) < 1:
        b1 = 0
    else:
        b1 = tuple_b[0]

    if len(tuple_a) < 2:
        a2 = 0
    else:
        a2 = tuple_a[1]

    if len(tuple_b) < 2:
        b2 = 0
    else:
        b2 = tuple_b[1]

    sum1 = a1 + b1
    sum2 = a2 + b2
    return (sum1, sum2)
