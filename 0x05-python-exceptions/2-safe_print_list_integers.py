#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    ll = 0
    try:
        for i in range(x):
            ll += 1
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="\n" if ll == x - 1 else "")
                count += 1
    except TypeError:
        pass
    return count
