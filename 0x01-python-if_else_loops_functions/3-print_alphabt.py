#!/usr/bin/python3

for a in range(97, 123):
    if chr(a) != 'e' or chr(a) != 'q':
        print("{}" .format(chr(a)), end='')
