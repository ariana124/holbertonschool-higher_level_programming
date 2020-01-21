#!/usr/bin/python3
"""
Module that contains the function from_json_string
"""
import json


def from_json_string(my_str):
    """ returns an object(data structure) represented by a JSON string """
    return json.loads(my_str)
