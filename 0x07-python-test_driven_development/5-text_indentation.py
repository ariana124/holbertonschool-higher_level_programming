#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    schar = ['.', '?', ':']
    for c in text:
        string += c
        if c in schar:
            print(string.strip())
            print()
            string = ""
    print(string.strip(), end='')
