#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    for i, x in enumerate(argv[1:]):
        sum = sum + int(argv[i + 1])
    print("{}".format(sum))
