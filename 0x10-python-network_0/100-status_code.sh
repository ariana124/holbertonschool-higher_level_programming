#!/bin/bash
# sends a request that sends a status with the http return code
curl -so /dev/null -w "%{http_code}" "$1"
