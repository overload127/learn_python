#!/usr/bin/env python3

import random


def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "data/forenames.txt"),
                            (surnames, "data/surnames.txt")):
        for name in open(filename, encoding="utf8"):
            names.append(name.rstrip())
    return forenames, surnames

forenames, surnames = get_forenames_and_surnames()
fh = open("test-names1.txt", "w", encoding="utf8")
for i in range(100):
    line ="{0:.20} {1:.20}\n".format(random.choice(forenames),
                             random.choice(surnames))
    fh.write(line)
    print(line)

fh.close() 
