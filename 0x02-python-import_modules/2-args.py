#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = len(sys.argv)
    if count == 1:
        print("No argument(s).")
    elif count == 2:
        print("1 argument: ")
    else:
        print("{:d} arguments: ".format(count - 1))

    for arg in range(1, count):
        print("{:d}: {:s}".format(arg, sys.argv[arg]))
