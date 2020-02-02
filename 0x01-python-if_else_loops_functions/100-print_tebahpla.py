#!/usr/bin/python3

for c in range(ord('z'), (ord('a') - 1), - 1):
    letter = c if c % 2 == 0 else c - 32
    print("{}".format(chr(letter)), end='')
