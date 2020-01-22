#!/usr/bin/env python3
# -smrH -o size "C:\\Users\\kostya\\py3eg\\learn_python\\book1\\GL_5"
# Программа работает как dir из винды или ls из линукса.
# Есть косяк) при сортировке по имени с рекурсией учитывает буквы пути к файлу.
# Решение - сделать доп-поле в словаре для путя, и производить склеивание строк перед самым выводом.

import optparse
import collections
import os
import time
import locale

SIZE, FILE_NAME, MODIFIED = 0, 1, 2

def main():
    opts, args = init_optparse()
    path_dirs = [line.replace("\\", "/") for line in args]

    locale.setlocale(locale.LC_ALL, "")

    for path_dir in path_dirs:
        data_files = collections.defaultdict(list)
        count_files, count_dir = 0, 0
        if opts.recursive:
            count_files, count_dir = from_walk(data_files, path_dir, opts.hidden)
        else:
            count_files, count_dir = from_listdir(data_files, path_dir, opts.hidden)

        if      opts.order in ("name", "n"):
            #sort_fun = lambda flag: flag[FILE_NAME].lower() if flag[FILE_NAME].rfind("/") == -1 else flag[FILE_NAME][flag[FILE_NAME].rfind("/")+1:].lower()
            sort_fun = lambda flag: flag[FILE_NAME][flag[FILE_NAME].rfind("/")+1:]
        elif    opts.order in ("modified", "m"):
            sort_fun = lambda flag: flag[MODIFIED]
        elif    opts.order in ("size", "s"):
            sort_fun = lambda flag: flag[SIZE]
        else:
            print("Случилось невозможное. Это связано с выбором сортировки")
            exit(2)

        line_file = []
        line_folder = []
        for key_word in sorted(data_files):
            for line in sorted(data_files[key_word], key=sort_fun):
                print_line = ""
                if opts.modified:
                    print_line = "{0:20} ".format(time.strftime(
                        '%Y-%m-%d %H:%M:%S',time.gmtime(line[MODIFIED])))
                if opts.sizes:
                    print_line = "".join((print_line, "{0:10n} ".format(line[SIZE]) ))
                print_line = "".join((print_line, "{0:<}".format(line[FILE_NAME]) ))
                line_file.append(print_line)
            
            if key_word != path_dir:
                print_line = ""
                if opts.modified:
                    print_line = "{0:20} ".format("")
                if opts.sizes:
                    print_line = "".join((print_line, "{0:10} ".format("") ))
                print_line = "".join((print_line, "{0:<}".format(key_word) ))
                line_folder .append(print_line)

        for line in line_file:
            print(line)
        for line in line_folder:
            print(line)
        
        print("{0} files, {1} directory".format(count_files, count_dir))

def init_optparse():
    """Функция читает параметры запуска программы и возвращает их.

        Входные параметры:
            -нет
        Возвращает:
            Кортеж из двух списков

            Первый список - это набор параметров, которые
            читает и обрабатывает функция.

            Второй список - это список из строк,
            хранящие параметры, несовпадающие
            ни с одним предопределённым для данной программы.
    """

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
    parser.set_defaults(hidden=False, modified=False, order="name",
                        recursive=False, sizes=False)
    opts, args = parser.parse_args()
    
    if not args:
        args = ["."]
    return opts, args


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
