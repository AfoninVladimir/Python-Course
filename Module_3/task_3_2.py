"""Напишите проверку на то, является ли строка палиндромом.
 Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево. (довод там и т.п.)"""

s = "Аргентина манит негра"
s2 = s.lower().replace(" ", "")
if s2 == s2[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")