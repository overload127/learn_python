#!/usr/bin/env python3

def main():
    x = int(input("Введите число: "))
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

main()
