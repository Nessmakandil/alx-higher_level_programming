#!/usr/bin/python3

def uniq_add(my_list=[]):
    occurrence = []
    for i in my_list:
        if i not in occurrence:
            occurrence.append(i)
    sum = 0
    for i in occurrence:
        sum += i
    return (sum)
