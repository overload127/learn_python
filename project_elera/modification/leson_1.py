#!/usr/bin/env python3

import optparse

START = 0
STOP = 10

def main():
    opts, args = init_optparse()
    sum = 0
    for i in range(opts.start, opts.stop):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print("Сума чисел от {0} до {1} равна = [{2}]".format(
        opts.start, opts.stop, sum))


def init_optparse():
    """Функция читает параметры запуска программы и возвращает их

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
    parser = optparse.OptionParser(usage="Usage: %prog [options]")
    parser.description = "========================="
    
    parser.add_option("-s", "--start", dest="start", type="int",
            help=("Устанавливает начальное значение [default: %default]"))
    parser.add_option("-S", "--stop", dest="stop", type="int",
            help=("Устанавливает конечное значение [default: %default]"))
    
    parser.set_defaults(start=START, stop=STOP)
    return parser.parse_args()

main()
