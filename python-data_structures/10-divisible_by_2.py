#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    r = []
    for i in my_list:
        r.append(i % 2 == 0)
    return r
