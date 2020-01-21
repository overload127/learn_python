#!/usr/bin/env python3

def main():
    x=3
    y=5
    print("X={0} Y={1}".format(x, y))
    x_y(x,y)
    print("X={0} Y={1}".format(x, y))

def x_y(x, y):
    x+=y

main()
