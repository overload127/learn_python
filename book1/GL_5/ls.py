#!/usr/bin/env python3
# "C:\\Users\\kostya\\py3eg\\learn_python\\book1\\GL_5"
# Программа работает как dir из винды или ls из линукса.
# Есть косяк) при сортировке по имени с рекурсией учитывает буквы пути к файлу.
# Решение - сделать доп-поле в словаре для путя, и производить склеивание строк перед самым выводом.

import optparse
import collections
import os
import time
import locale

SORT_BY_NAME, SORT_BY_MODIFIED, SORT_BY_SIZE = 1, 2, 3

def main():
    parser = optparse.OptionParser(usage="Usage: %prog [options] [path1 [path2 [... pathN]]]")
    parser.description = "The paths are optional; if not given . is used."
    parser.add_option(  "-H", "--hidden", action="store_true", dest="hidden",
                        help=("show hidden files [default: %default]"))
    parser.add_option(  "-m", "--modified", action="store_true", dest="modified",
                        help=("show last modified date/time [default: %default]"))
    parser.add_option(  "-o", "--order", action="store", type="choice", dest="order",
                        choices=["name", "n", "modified", "m", "size", "s"],
                        help=("order by ('name', 'n', 'modified', 'm', 'size', 's') [default: %default]"))
    parser.add_option(  "-r", "--recursive", action="store_true", dest="recursive",
                        help=("recurse into subdirectories [default: %default]"))
    parser.add_option(  "-s", "--sizes", action="store_true", dest="sizes",
                        help=("show sizes [default: %default]"))
    parser.set_defaults(hidden=False, modified=False, order="name", recursive=False, sizes=False)
    opts, args = parser.parse_args()
    if args:
        path_dirs = [line.replace("\\", "/") for line in args]
    else:
        path_dirs = ["."]

    locale.setlocale(locale.LC_ALL, '')

    for path_dir in path_dirs:
        data_files = collections.defaultdict(list)
        count_files, count_dir = 0, 0
        if opts.recursive:
            count_files, count_dir = from_walk(data_files, path_dir, opts.hidden)
        else:
            count_files, count_dir = from_listdir(data_files, path_dir, opts.hidden)

        files_list = []
        for line in data_files.values():
            files_list.extend(line)

        if      opts.order in ("name", "n"):
            sort_fun = lambda flag: flag[1].lower()
        elif    opts.order in ("modified", "m"):
            sort_fun = lambda flag: flag[2]
        elif    opts.order in ("size", "s"):
            sort_fun = lambda flag: flag[0]
        else:
            print("Случилось невозможное. Это связано с выбором сортировки")
            exit(2)
        files_list

        for line in sorted(files_list, key=sort_fun):
            print_line = ""
            if opts.modified:
                print_line = "{0:20} ".format(time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(line[2])))
            if opts.sizes:
                print_line = "".join((print_line, "{0:10n} ".format(line[0])))
            print_line = "".join((print_line, "{0:<}".format(line[1])))     
            print(print_line)

        for key in sorted(data_files):
            if key != path_dir:
                print_line = ""
                if opts.modified:
                    print_line = "{0:20} ".format("")
                if opts.sizes:
                    print_line = "".join((print_line, "{0:10} ".format("")))
                print_line = "".join((print_line, "{0:<}".format(key)))
                print(print_line)

        print("{0} files, {1} directory".format(count_files, count_dir))
    
def from_walk(data_files, path_dir, hidden=False):
    count_files, count_dir = 0, 0
    for root, dirs, files in os.walk(path_dir):
        root = root.replace("\\", "/")
        count_dir += len(dirs)
        for filename in files:
            if filename[0] == "." and not hidden:
                continue
            fullname = (os.path.join(root, filename)).replace("\\", "/")
            (data_files[root]).append([os.path.getsize(fullname), fullname, os.path.getmtime(fullname)])
            count_files += 1
        for dirname in dirs:
            if dirname[0] == "." and not hidden:
                continue
            if data_files["".join((root, "/", dirname.replace("\\", "/")))]:
                pass

    return (count_files, count_dir)


def from_listdir(data_files, path_dir, hidden=False):
    count_files, count_dir = 0, 0
    print(path_dir)
    for name_file in os.listdir(path_dir):
        if name_file[0] == "." and not hidden:
            continue
        if os.path.isfile(name_file):
            count_files += 1
            fullname = "".join((path_dir, "/", name_file))
            (data_files[path_dir]).append([os.path.getsize(fullname), fullname, os.path.getmtime(fullname)])
        elif os.path.isdir(name_file):
            count_dir += 1
            if data_files["".join((path_dir, "/", name_file))]:
                pass
    
    return (count_files, count_dir)

main()
