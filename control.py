#!/usr/bin/env python3

import sys, pickle

inputfile = sys.argv[1]

controlchars = pickle.load(open('lib/control.p', 'rb'))

print([x[0] for x in controlchars])

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
        charcheck(bytes, [x[0] for x in controlchars])

