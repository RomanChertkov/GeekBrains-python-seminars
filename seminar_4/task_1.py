"""
Вычислить число Pi c заданной точностью d, не используя ф. round()
"""

import os
import math

os.system('clear')

def my_round(number: float, numbers_of_digits:int)->float:
    """ Custom round"""
    last_digit = int(PI*10**(numbers_of_digits+1) % 10)

    ratio = 10**numbers_of_digits

    if last_digit < 5:
        return number*ratio // 1 / ratio

    return (number*ratio+1) // 1 / ratio

PI   = math.pi
input_number = int(input("Введите количество знаков после запятой:"))
print(round(PI,input_number), "Стандартная ф-я round")
print (my_round(PI,input_number),"Кастомная ф-я my_round")
