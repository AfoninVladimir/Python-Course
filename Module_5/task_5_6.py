"""Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись
 вида Покупатель товар количество, где Покупатель — имя покупателя (строка без пробелов), товар — название товара
 (строка без пробелов), количество — количество приобретенных единиц товара.
Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им
 единиц каждого вида товаров. Список покупателей, а также список товаров для каждого покупателя нужно
 выводить в лексикографическом порядке."""

file_input = open("task_5_6(input).txt", "r")
file_output = open("task_5_6(output).txt", "w")
s = file_input.read().split("\n")

for i in range(len(s)):
    s[i] = s[i].split(" ")

# сортировка
for i in range(len(s)):
    for j in range(len(s) - 1 - i):
        if s[j][0] > s[j+1][0]:
            s[j], s[j+1] = s[j+1], s[j]
        elif s[j][0] == s[j+1][0]:
            if s[j][1] > s[j + 1][1]:
                s[j], s[j + 1] = s[j + 1], s[j]

for i in range(len(s)):
    s[i] = " ".join(s[i])

result = dict()

# создание словаря
for i in s:
    k = i.split()
    if k[0] not in result.keys():
        result[k[0]] = {k[1]: int(k[2])}
    else:
        if k[1] in result[k[0]]:
            result[k[0]][k[1]] += int(k[2])
        else:
            result[k[0]].update({k[1]: int(k[2])})

for i in result:
    file_output.write(i + "\n")
    for j in result.get(i):
        file_output.write(j + " " + str(result.get(i).get(j)) + "\n")

file_input.close()
file_output.close()
