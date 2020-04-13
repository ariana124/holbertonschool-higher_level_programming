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

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})

    r_json = response.json()

    if response.headers.get('content-type') is 'application/json':
        print("Not a valid JSON")
    elif len(r_json) == 0:
        print("No result")
    else:
        print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
