#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    elif len(sys.argv) - 1 == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} argument:".format(len(sys.argv) - 1))
        for i, x in enumerate(sys.argv[1:]):
            print("{}: {}".format(i + 1, x))
