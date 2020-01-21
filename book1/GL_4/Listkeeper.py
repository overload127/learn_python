#!/usr/bin/env python3

import os

def main():
    default = "o"
    files = loadfile()
    while True:
        print_files_name(files)
        select = get_string("[A]dd [D]elete [O]pen [Q]uit",
                            default=default, minimum_lenght=1, maximum_lenght=10)
        if not select:
            select = default
        else:
            old_default = default
            default = select
        if select.lower() in {"a", "add"}:
            if addfile():
                files = loadfile()
        elif select.lower() in {"d", "delete"}:
            if len(files) > 0:
                remove_file(files)
                files = loadfile()
            else:
                print("Нет файлов для удаления")
        elif select.lower() in {"o", "open"}:
            if len(files) > 0:
                if len(files) == 1:
                    openfile(files[0])
                else:
                    number = get_integer("Введите номер файла, который нужно открыть или 0 для отмены",
                                         name="integer", default=1, minimum=1,
                                         maximum=len(files), allow_zero=True)
                    if number > 0:
                        number -= 1
                        openfile(files[number])
            else:
                print("Нет подходящих файлов для открытия.")
        elif select.lower() in {"q", "quit"}:
            break
        else:
            default = old_default
            print("I don't understand what do you write. Try again please.")

def openfile(direct):
    default = "a"
    list_line = loadlines(direct)
    save = False
    while True:
        print_lines(list_line)
        select = get_string("[A]dd {0}[D]elete [Q]uit".format("[S]ave "if save else ""),
                            default=default, minimum_lenght=1, maximum_lenght=10)
        if not select:
            select = default
        else:
            old_default = default
            default = select

        if select.lower() in {"a", "add"}:
            line = get_string("Add item", minimum_lenght=1, maximum_lenght=30)
            if line:
                list_line.append(line)
                save = True
        elif select.lower() in {"s", "save"} and save:
            savefile(direct, list_line)
            save = False
        elif select.lower() in {"d", "delete"}:
             number = get_integer("Введите номер элемента, который нужно удалить или 0 для отмены",
                                  name="integer", default=1, minimum=1,
                                  maximum=len(list_line), allow_zero=True)
             if number > 0:
                 number -= 1
                 del(list_line[number])
                 save = True
        elif select.lower() in {"q", "quit"}:
            break
        else:
            default = old_default
            print("I don't understand what do you write. Try again please.")
    if save:
        savefile(direct, list_line)
                
                
def savefile(direct, line_list):
    try:
        f = open(direct, 'r+')
        for item in line_list:
            print(item, file=f)
    except:
        print("ERROR!!!")
    finally:
        f.close()

def loadlines(direct):
    if os.path.exists(direct):
        try:
            f = open(direct, 'r+')
            list_line = list()
            for i, line in enumerate(f, start = 1):
                list_line.append(line.rstrip())
            if len(list_line) == 0:
                print("no items are in the list")
            else:
                list_line.sort()
        except:
            print(direct)
            print("ERROR!!!")
        finally:
            if fh is not None:
                f.close()
            return list_line
    else:
        print("Файла {0} нет.".format(direct))
        return list_line
    
def loadfile(direct=None):
    files = list()
    while len(files) == 0:
        if direct:
            files = os.listdir(direct)
        else:
            files = os.listdir()

        files = list(filter(lambda line: False if not line.endswith((".lst")) else True, files))

        if len(files) == 0:
            print("Нет ни одного подходящего файла.")
            while addfile() == False:
                pass
        else:
            files.sort()
            break

    return files

def addfile():
    name = get_string("Input name file",
                      default="temp.lst", minimum_lenght=1, maximum_lenght=25)  
    if name is None or len(name.lstrip()) == 0:
        print("Не правильное имя файла.")
        return False
    if not name.endswith((".lst")):
        name = "".join((name, ".lst"))
    f = open(name, 'w')
    f.close()
    return True

def remove_file(files):
    number = get_integer("Введите номер файла, который нужно удалить или 0 для выхода",
                         name="integer", default=1, minimum=1,
                         maximum=len(files), allow_zero=True)
    if number > 0:
        number -= 1
        try:
            os.remove(files[number])
        except FileNotFoundError as err:
            print("Не удалось удалить файлб т.к. его нет.")

def print_files_name(files):
    i_wight = 0
    if len(files) < 10:
        i_wight = 1
    elif len(files) < 100:
        i_wight = 2
    else:
        i_wight = 3
    for i, line in enumerate(files, start=1):
        print("{0:{wh}} {1}".format(i, line, wh=i_wight))

def print_lines(list_lines):
    i_wight = 0
    if len(list_lines) < 10:
        i_wight = 1
    elif len(list_lines) < 100:
        i_wight = 2
    else:
        i_wight = 3
    for i, line in enumerate(list_lines, start=1):
        print("{0:{wh}} {1}".format(i, line, wh=i_wight))    

def get_string(message, name="string", default=None,
               minimum_lenght=0, maximum_lenght=80):    
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_lenght == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(name))
            if not (minimum_lenght <= len(line) <= maximum_lenght):
                raise ValueError("{0} must have at least {1} and "
                                 "at most {2} characters".format(
                                     name, minimum_lenght, maximum_lenght))
            return line
        except ValueError as err:
            print("ERROR", err)

def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):

    class RangeError(Exception): pass

    message += ": "if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be empty".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{0} must be between {1} and {2}"
                                 "inclusive {3}".format(name, minimum, maximum,
                                                       (" (or 0)" if allow_zero else "")))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))


main()
