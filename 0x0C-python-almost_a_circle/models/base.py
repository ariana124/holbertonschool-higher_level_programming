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
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

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

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        dummy = {}
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                mylist = f.read()
        except:
            return []

        all_inst = []
        newlist = cls.from_json_string(mylist)
        for i in newlist:
            all_inst.append(cls.create(**i))
        return all_inst
