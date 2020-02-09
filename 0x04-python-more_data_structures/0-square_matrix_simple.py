#!/usr/bin/python3
"""
Module that contains the function square_matrix_simple
"""


def square_matrix_simple(matrix=[]):
        """ computes the square value of all integers in a matrix """
        return ([[x**2 for x in row] for row in matrix])
