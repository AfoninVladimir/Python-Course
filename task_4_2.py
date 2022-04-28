"""Найдите три ключа с самыми высокими значениями в словаре"""

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
keys = []
val = 0
key = ""
for i in range(3):
    for k, v in my_dict.items():
        if k in keys:
            continue
        else:
            if v > val:
                val = v
                key = k
    keys.append(key)
    val = 0
    key = ""

print(* [i for i in keys], sep = ", ")
