#!/usr/bin/python3


def matrix_divided(matrix, div):
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    m = "matrix must be a matrix (list of lists) of integers/floats"
    for y in matrix:
        if not isinstance(y, list):
            raise TypeError(m)
        for x in y:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError(m)

    for y in range(1, len(matrix)):
        if len(matrix[y]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    return [[(round(x / div, 2))for x in y] for y in matrix]
