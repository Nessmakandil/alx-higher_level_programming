#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key in a_dictionary.keys():
        new_dictionary[key] = 2 * a_dictionary.get(key)
    return (new_dictionary)
