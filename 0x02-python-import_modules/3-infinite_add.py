#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    count = len(sys.argv)
    for i in range(1, count):
        sum = sum + int(sys.argv[i])
    print("{:d}".format(sum))
