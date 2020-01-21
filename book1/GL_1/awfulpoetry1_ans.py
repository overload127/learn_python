#! /usr/bin/env python3

import random

articles = ["the", "a", "an"]
syshs    = ["cat", "dog", "man", "woman"]
glagols  = ["sang", "ran", "jumped"]
narechs  = ["loudly", "quietly", "well", "badly"]

stroka = 5
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
