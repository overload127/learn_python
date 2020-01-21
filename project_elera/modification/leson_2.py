#!/usr/bin/env python3

import timeit
import optparse

START = 1
STOP = 4000000

def main():
    opts, args = init_optparse()   
    #print(timeit.timeit("fib1()", setup="from __main__ import fib1", number=100))   
    #print(timeit.timeit("fib2()", setup="from __main__ import fib2", number=100))
    print("Сумма чётных чисел ряда фибоначи от 1 до {0} равна [{1}]".format(opts.stop, fib1(opts.stop)))

def fib1(s=STOP):
    a = 1
    b = 2
    sum1 = b
    while a < s:
        a += b
        b += a
        if a % 2 == 0:
            sum1 += a
        elif b % 2 == 0:
            sum1 += b
    return sum1

def fib2():
    f = [1,2]
    i = 1
    a = 0
    while f[i] < 4000000:
        f.append(f[i-1] + f[i-2])
        i += 1
        a = f[i]
    return filter(lambda x: x % 2 == 0, f)
    


def init_optparse():
    parser = optparse.OptionParser(usage="Usage: %prog [options]")
    parser.description = "========================="
    
    parser.add_option("-s", "--stop", dest="stop", type="int",
            help=("Устанавливает конечное значение [default: %default]"))
    
    parser.set_defaults(stop=STOP)
    return parser.parse_args()

main()
