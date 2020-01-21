#!/usr/bin/env python3

import sys
import unicodedata

def print_unicode_table(words):
    print("decimal  hex  chr {0:^40}".format("name"))
    print("------- ----- --- {0:-<40}".format(""))

    code = ord(" ")
    end = sys.maxunicode

    count_slov = 0

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** uncnown ***")
        find_yes = True
        for word in words:
            if word not in name.lower():
                find_yes = False
                break
            
        if find_yes:
            print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
            count_slov += 1
        code += 1
    print("[{0}]".format(count_slov))


words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv[0]))
    else:
        for word in sys.argv[1:]:
            words += [word.lower()]
    print_unicode_table(words)
else:
    print_unicode_table(words)

