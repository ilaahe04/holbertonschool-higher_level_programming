#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    for i in set(my_list):
        count += i
    return count
