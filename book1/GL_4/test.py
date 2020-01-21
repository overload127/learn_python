#!/usr/bin/env python3
import collections


def main():
    lst = [1,2,3,4,5]
    #print(list_find1(lst,4))
    #print(list_find2(lst,6))
    line = "dsfdsfdsfsdfsdfs"
    for column, c in enumerate(line, start=1):
        print("[{0}] = [{1}]".format(column,c))

def list_find1(lst, target):
    for index, x in enumerate(lst):
        if x == target:
            break
        else:
            index = -1
    return index

def list_find2(lst, target):
    index = 0
    while index < len(lst):
        if lst[index] == target:
            break
        index += 1
    else:
        index = -1
    return index


#main()

def iii():
    return -1

m1 = collections.defaultdict(lambda: -2)
print(m1["test"])
