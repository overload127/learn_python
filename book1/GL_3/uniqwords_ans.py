#!/usr/bin/env python3

import string
import sys
import collections


def by_value(w):
    return w[1]

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1

for word, count in sorted(words.items(), key=by_value):
    print("'{0:20}' occurs {1:3} times".format(word, count))
