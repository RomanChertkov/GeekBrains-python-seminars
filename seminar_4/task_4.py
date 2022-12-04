"""
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена
и записать в файл (или вывести в терминал) многочлен степени k.
"""

import os
import random

def generate_polynomial(ratios: list[int])-> str:
    """generate polynomial"""
    polynomial = ''
    lenth = len(ratios)

    for i in range(lenth):
        if i == 0:
            polynomial+= f"{ratios[i]}"
        elif i == 1:
            polynomial+=f" + {ratios[i]}*x"
        else:
            polynomial+=f" + {ratios[i]}*x^{i}"

    return polynomial

os.system('clear')

input_number = int(input("Введите степень: "))

random_ratios = [random.randint(0,100) for i in range(input_number+1)]
print(random_ratios)
print(generate_polynomial(random_ratios))
