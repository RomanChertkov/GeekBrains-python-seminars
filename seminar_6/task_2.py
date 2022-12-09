"""
Дан список, вывести отдельно буквы и цифры, пользуясь filter.
[12,'sadf',5643] ---> ['sadf'] ,[12,5643]
"""

import os

os.system("clear")

elements = list(
    map(
        lambda el: int(el) if el.isdigit() else el,
        input("Введите список: ").split()
    )
)

numbers = list(filter(lambda el: isinstance(el, int), elements))
strings = list(filter(lambda el: isinstance(el, str), elements))

print ("Исходный список ", elements)
print(strings, numbers, sep=", ")
