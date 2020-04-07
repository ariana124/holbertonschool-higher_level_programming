#!/bin/bash
# script that takes in a URL & displays all HTTP methods the server will accept
curl -sI OPTIONS "$1" | grep "Allow:" | cut --complement -f1 -d" "
