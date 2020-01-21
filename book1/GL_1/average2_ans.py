#! /usr/bin/env python3

count   = 0
summa   = 0
minimum = None
maximum = None
sred    = 0
mediana = 0
numbers = []

while True:
    try:
        line = input("enter a number or Enter to finish:") 
        if not line:
            break
        else:
            numbers += [int(line)]
            count += 1
            summa += numbers[count-1]
            if not minimum or minimum > numbers[count-1]:
                minimum = numbers[count-1]
            if not maximum or maximum < numbers[count-1]:
                maximum = numbers[count-1]
    except ValueError as err:
        print(err)

if count:
    sred = summa / count

    i = 0
    while i < count:
        k = i + 1
        while k < count:
            if numbers[i] > numbers[k]:
                dop = numbers[i]
                numbers[i] = numbers[k]
                numbers[k] = dop
            k += 1
        i += 1

    med_indx = int(count / 2)
    if med_indx == (count) / 2:
        mediana = (numbers[med_indx-1] + numbers[med_indx]) / 2
    else:
        mediana = numbers[med_indx-1]

print("numbers:", numbers)
print("count =", count, " sum =", summa, " lowest =", minimum, "highest =", maximum, " mean =", sred, "mediana =", mediana)
