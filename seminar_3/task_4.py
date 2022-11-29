"""
Программа будет преобразовывать десятичное число в двоичное.
"""

import os
import random

os.system('clear')

random_number = random.randint(0, 10)

print (
    "Десятичное число",random_number ,
    "в двоичной системе счисления",bin(random_number)[2:]
)
