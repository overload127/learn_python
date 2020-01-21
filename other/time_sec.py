#!/usr/bin/env python3
import timeit
 
 
def test():
    res = " ".join(('начало', 'середина', 'конец'))
 
 
def test1():
    res = '{} {} {} '.format('начало', 'середина', 'конец')
 
 
def test2():
    res = 'начало' + 'середина' + 'конец'
 
 
print(timeit.timeit("test()", setup="from __main__ import test", number=100000))
print(timeit.timeit("test1()", setup="from __main__ import test1", number=100000))
print(timeit.timeit("test2()", setup="from __main__ import test2", number=100000))
