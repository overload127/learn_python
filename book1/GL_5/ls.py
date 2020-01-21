#!/usr/bin/env python3

import optparse
import collections
import os
import time

SORT_BY_NAME, SORT_BY_MODIFIED, SORT_BY_SIZE = 1, 2, 3

def main():
    parser = optparse.OptionParser(usage="Usage: %prog [options] [path1 [path2 [... pathN]]]")
    parser.description = "The paths are optional; if not given . is used."
    parser.add_option("-H", "--hidden", action="store_true", dest="hidden",
            help=("show hidden files [default: %default]"))
    parser.add_option("-m", "--modified", action="store_true", dest="modified",
            help=("show last modified date/time [default: %default]"))
    parser.add_option("-o", "--order", action="store", type="choice", dest="order",
                      choices=["name", "n", "modified", "m", "size", "s"],
            help=("order by ('name', 'n', 'modified', 'm', 'size', 's') [default: %default]"))
    parser.add_option("-r", "--recursive", action="store_true", dest="recursive",
            help=("recurse into subdirectories [default: %default]"))
    parser.add_option("-s", "--sizes", action="store_true", dest="sizes",
            help=("show sizes [default: %default]"))
    parser.set_defaults(maxwidth=100, format=".0f", hidden=False,
                        modified=False, order="name", recursive=False, sizes=False)
    opts, args = parser.parse_args()



    data = collections.defaultdict(int)
    count_files, count_dir = 0, 0

    count_files, count_dir = from_walk(count_files, count_dir, data)

    for size, filename, date_file in sorted(data):
        if date_file:
            date_file = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(date_file))
    
        print("{0:20} {1:10} {2:<}".format(date_file,size, filename))

    
            
    print("{0} files, {1} directory".format(count_files, count_dir))
    
def from_walk(count_files, count_dir, data):
    for root, dirs, files in os.walk("."):
        if root != ".":
            key = (None,None,root)
            data[key] = 1
        for filename in files:
            fullname = os.path.join(root, filename)
            key = (os.path.getsize(fullname), filename, os.path.getmtime(fullname))
            data[key] = 1
            print("root = {0}".format(root))
            print("dirs = {0}".format(dirs))
            print("files = {0}".format(files))
            count_files += 1

            count_dir += 1

    return (count_files, count_dir)


def from_listdir(count_files, count_dir, data):
    for root, dirs, files in os.walk("."):
        for filename in files:
            fullname = os.path.join(root, filename)
            key = (os.path.getsize(fullname), filename, os.path.getmtime(fullname))
            data[key] = 1
            if os.path.isfile(fullname):
                count_files += 1
            else:
                count_dir += 1

    return (count_files, count_dir)

    
main()
