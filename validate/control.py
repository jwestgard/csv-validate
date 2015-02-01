#!/usr/bin/env python3

import sys

inputfile = sys.argv[1]

controlchars = [b'\x00', b'\x01', b'\x02', b'\x03', b'\x04', b'\x05', b'\x06', b'\x07', b'\x08', b'\x09', b'\x0a', b'\x0b', b'\x1c', b'\x1d', b'\x1e', b'\x1f', b'\x10', b'\x11', b'\x12', b'\x13', b'\x14', b'\x15', b'\x16', b'\x17', b'\x18', b'\x19', b'\x1a', b'\x1b', b'\x1c', b'\x1d', b'\x1e', b'\x1f']

def charcheck(mystring, chars):
    for c in chars:
        if c in mystring:
            charlocation = mystring.find(c)
            print("Found {0} at {1}".format(c, charlocation))

with open(inputfile, 'r') as f:
    for n, line in enumerate(f):
        print("\nLine {0}".format(n))
        print("========")
        line = line.rstrip('\n')
        print("String -> {0}".format(line))
        bytes = str.encode(line)
        print("Bytes -> {0}".format(bytes))
        charcheck(bytes, controlchars)

