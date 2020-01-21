#!/usr/bin/env python3

import string
import sys
import collections


sites = collections.defaultdict(int)
for filename in sys.argv[1:]:
    for line in open(filename, "r", encoding="utf-8"):
        i = 0
        while True:
            site = None
            i = line.find("http://", i)
            if i > -1:
                i += len("http://")
                for j in range(i, len(line)):
                    if not (line[j].isalnum() or line[j] in ".-"):
                        site = line[i:j].lower()
                        break
                if site and "." in site:
                    #sites.setdefault(site,set()).add(filename)
                    sites[site] = filename
                i = j
            else:
                break

for site in sorted(sites):
    print("{0} is referred to in:".format(site))
    for filename in sorted(sites[site], key=str.lower):
        print("    {0}".format(filename))
