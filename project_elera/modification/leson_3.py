#!/usr/bin/env python3

import timeit
import optparse
import math

def main():
    opts, args = init_optparse()
    if opts.stop == None:
        x = int(input("Введите число: "))
    else:
        x = opts.stop
    #print(timeit.timeit("issimple1()", setup="from __main__ import issimple1", number=1000))
    #print(timeit.timeit("issimple2()", setup="from __main__ import issimple2", number=1000))
    simple_line = issimple1(x)
    print(simple_line)
    print(max(simple_line))

    
# Моя функция
def issimple1(x = 1000):
    simple_line = []
    while x != 1:
        for i in range(2, x + 1):
            if x % i == 0:
                simple_line.append(i)
                x //= i
                break
    return simple_line

# Чужая функция. Нужна для засечения времени
def issimple2(a = 1000):
    r=math.ceil(math.sqrt(a))
    lst=[]
    for i in range(3,r):
        if a%i==0:
            if issimple2(i)==[]:
                lst.append(i)
    return lst

def init_optparse():
    parser = optparse.OptionParser(usage="Usage: %prog [options]")
    parser.description = "========================="
    
    parser.add_option("-s", "--stop", dest="stop", type="int",
            help=("Устанавливает конечное значение [default: %default]"))
    
    parser.set_defaults(stop=None)
    return parser.parse_args()

main()
