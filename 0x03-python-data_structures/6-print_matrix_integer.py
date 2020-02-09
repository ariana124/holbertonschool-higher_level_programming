#!/usr/bin/python3
"""
Module containing the function print_matrix_integer
"""


def print_matrix_integer(matrix=[[]]):
    """ prints a matrix of integers """
    for row in matrix:
        print(" ".join("{:d}".format(int) for int in row))
