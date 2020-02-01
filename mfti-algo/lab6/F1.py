#!/usr/bin/env python3

def test(x):
    tt = 3**(x//2) + (x-2) + (x-2-2)*3 * 2 
    return tt

def test2(x, i=1):
    if(x>=2):
        tt = 3*test2(x-2, i=1)
    else:
        tt = 1
    return tt

#print(test2(2))
#print(test2(4))
#print(test2(6))


n = int(input())
a, b, c = 1, 3, 0
if n%2 == 1:
    b = 0
else:
    for i in range(1, n//2):      
        c = 4*b - a
        a = b
        b = c
print(b)
