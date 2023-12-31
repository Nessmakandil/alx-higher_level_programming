#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    ll = 0
    try:
        for i in range(x):
            ll += 1
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except TypeError:
        pass
    finally:
        print(end="\n")
    return count
