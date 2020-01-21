#!/usr/bin/env python3
#grepword.py

import sys


if len(sys.argv) < 3:
    print("usage: {0} word infile1 [infile2 [... infileN]]".format(sys.argv[0][sys.argv[0].rfind("/")+1:]))
    sys.exit()

word = sys.argv[1]
for filename in sys.argv[2:]:
    for lino, line in enumerate(open(filename), start=1):
        if word in line:
            print("{0}:{1}:{2:.40}".format(filename, lino, line.rstrip()))
