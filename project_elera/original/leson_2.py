#!/usr/bin/env python3

def main():
    print("Сумма четных чисел ряда фибоначи начиная от {0} до {1} равна [{2}]".format(1, 4000000, fib()))
    
def fib():
    a = 1
    b = 2
    sum1 = b
    while a < 4000000:
        a += b
        b += a
        if a % 2 == 0:
            sum1 += a
        elif b % 2 == 0:
            sum1 += b
    return sum1

main()
