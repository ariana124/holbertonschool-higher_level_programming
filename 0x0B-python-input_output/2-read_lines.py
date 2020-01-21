#!/usr/bin/python3
"""
Module that contains the function read_lines
"""


def read_lines(filename="", nb_lines=0):
    """ reads the lines of a text file and prints it to stdout """
    counter = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if nb_lines <= 0 or nb_lines > counter:
                print(line, end='')
                counter += 1
