#!/usr/bin/python3
"""
Module that defines the class MyList that inherits from  class list
"""


class MyList(list):
    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
