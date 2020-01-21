#!/usr/bin/env python3
#C:\py3eg\book1\GL_2>csv2html2_ans.py < data/co2-sample.csv > co2-smple.html

import sys
import xml.sax.saxutils

def main():
    param = process_options(sys.argv)
    if param[0] != None:
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, param[0], param[1])
                count += 1
            except EOFError:
                break
        print_end()

def print_start():
    print("<table border='1'>")

def print_line(line, color, maxwidth, form):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:{1}}</td>".format(x,form))
            except ValueError:
                field = field.title()
                field = field.replace(" And", " and")
                field = xml.sax.saxutils.escape(field)
                if len(field) <= maxwidth:
                    print("<td>{0}</td>".format(field))
                else:
                    print("<td>{0:.{1}} ...</td>".format(field, maxwidth))
    print("</tr>")

def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:   # начало строки в кавычках
                quote = c
            elif quote == c:    # конец строки в кавычках
                quote = None
            else:
                field += c      # другая кавычка внутри строки в кавычках
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c          # добавить символ в поле
    if field:
        fields.append(field)    # добавить последнее поле в список
    return fields

def print_end():
    print("</table>")

def process_options(line):
    maxwidth = 100
    form = ".0f"
    if len(line) > 1:
        if line[1] in ("-h", "--help"):
            print("usage:"
                  "\ncsv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html"
                  "\nmaxwidth - необязательное целое число. Если задано, определяет максимальное число"
                  " символов для строковых полей. В противном случае используется значение по умолчанию {1}."
                  "\n"
                  "\nformat - формат вывода чисел. Если не заданоб по умолчанию используется формат \"{2}\".".format(line[0], maxwidth, form))
            return None, None
        else:
            for word in line[1:]:
                if word.startswith("maxwidth"):
                    try:
                        maxwidth = int(word[word.index("=")+1:])
                    except ValueError:
                        maxwidth = 100
                elif word.startswith("format"):
                    form = word[word.index("=")+1:]
    
    return maxwidth, form


main()
