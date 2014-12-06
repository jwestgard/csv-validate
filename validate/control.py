#!/usr/bin/env python3

import sys, csvkit, curses.ascii

# inputfile = sys.argv[1]

controlchars = [b'\x00', b'\x01', b'\x02', b'\x03', b'\x04', b'\x05', b'\x06', b'\x07', b'\x08', b'\x09', b'\x0a', b'\x0b', b'\x1c', b'\x1d', b'\x1e', b'\x1f', b'\x10', b'\x11', b'\x12', b'\x13', b'\x14', b'\x15', b'\x16', b'\x17', b'\x18', b'\x19', b'\x1a', b'\x1b', b'\x1c', b'\x1d', b'\x1e', b'\x1f']

for c in controlchars:
	print(hex(c))
	
