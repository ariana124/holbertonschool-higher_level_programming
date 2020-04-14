#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    try:
        url = "http://0.0.0.0:5000/search_user"
        response = requests.post(url, data={'q': q})

        r_json = response.json()

        if "id" in r_json and "name" in r_json:
             print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
