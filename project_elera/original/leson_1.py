#!/usr/bin/env python3

def main(): 
    sum = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print("Сума чисел от {0} до {1} равна = [{2}]".format(
        0, 1000, sum))


main()
