#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    sorted_values = sorted(a_dictionary.values())
    val = list(a_dictionary.values())
    keys = list(a_dictionary.keys())
    idx = val.index(sorted_values[0])
    return (keys[idx - 1])