#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n1 = int(abs(number) / 10)
n2 = (abs(number) / 10)

if number > 0:
    n = int(round((n2 - n1) * 10))
else:
    n = -int(round((n2 - n1) * 10))

if n > 5:
    print(f"Last digit of {number} is {n} and is greater than 5")
elif n == 0:
    print(f"Last digit of {number} is {n} and is 0")
elif n < 6:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
