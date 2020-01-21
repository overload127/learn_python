#! /usr/bin/env python3

import random

while True:
    x = random.randint(1, 6)
    y = random.choice(["apple", "banana", "cherry", "durian"])
    print("x =", x, "y =", y)
    text = input("Выход(д - да / н - нет): ")
    if text == 'д' or text == "да":
        break;
