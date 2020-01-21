#! /usr/bin/env python3

import random
import sys

articles = ["the", "a", "an"]
syshs    = ["cat", "dog", "man", "woman"]
glagols  = ["sang", "ran", "jumped"]
narechs  = ["loudly", "quietly", "well", "badly"]

stroka = 5

try:
    number = int(sys.argv[1])
    if 10 >= number >= 0:
        stroka = number
    else
        print("lines must be 1-10 inclusive")
except IndexError:
    print("usage: awfulpoetry2_ans.py <number>")
except ValueError as err:
    print(err)
            
while stroka > 0:
    article = random.choice(articles)
    sysh    = random.choice(syshs)
    glagol  = random.choice(glagols)

    if random.randint(0, 1):
        narech  = random.choice(narechs)
        print(article, sysh, glagol, narech)
    else:
        print(article, sysh, glagol)

    stroka-=1
