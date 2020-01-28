#!/usr/bin/python3
"""
Module containing the class Base
"""
import json


class Base:
    """ the base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        l = []
        if list_objs is not None:
            for i in list_objs:
                l.append(cls.to_dictionary(i))

        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(l))
