#!/usr/bin/python3
for x in range(ord('a'), ord('z')+1):
    if x not in [ord('e'), ord('q')]:
        print("{}".format(chr(x)), end="")
