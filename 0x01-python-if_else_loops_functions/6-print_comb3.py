#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if (x != y) and (y > x):
            print("{:02d}".format(y + 10 * x),
                end='\n' if (x == 8 and y == 9) else ", ")
    