"""Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей,
и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей."""
# 12, 234, 4356, 567, 87, 657, 83, 24, 324, 4856, 2, 34, 23, 2134, 4273, 4, 223, 422, 33, 4234, 4, 2332, 523
my_list = input("ввод: ").split(", ")
a = 0

for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

for i in range(1, len(my_list) - 1):
    if my_list[i] > my_list[i - 1] and my_list[i] > my_list[i + 1]:
        a += 1

print(a)
