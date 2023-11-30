#!/usr/bin/python3
for x in range(ord('A'), ord('Z')+1):
    print("{}".format(chr(x)), end='\n' if chr(x) == 'Z' else '')