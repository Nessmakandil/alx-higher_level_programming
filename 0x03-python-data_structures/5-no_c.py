#!/usr/bin/python3

def no_c(my_string):
    temp = list(my_string)
    for i, x in enumerate(temp):
        if x == 'C' or x == 'c':
            temp[i] = ''
    my_string = ''.join(temp)
    return my_string
