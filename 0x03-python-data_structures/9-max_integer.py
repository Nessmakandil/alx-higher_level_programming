#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list):
        temp = my_list[0]
        for x in my_list:
            if x > temp:
                temp = x
        return (temp)
    else:
        return (None)
