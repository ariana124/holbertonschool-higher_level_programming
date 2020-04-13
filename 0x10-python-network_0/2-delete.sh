#!/bin/bash
# sends a delete request to the URL passed as the 1st argument
curl -sX DELETE "$1"
