"""
Программа найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
"""

import os
import random
import math

os.system('clear')

def pairs_multiply(numbers_list:list)->list:
    """Calculate pairs myltiply"""

    multiply_list = []
    list_length = len(numbers_list)

    for i in range(math.ceil(list_length/2)):
        multiply_list.append(
            numbers_list[i]*numbers_list[list_length-1-i]
        )

    return multiply_list

list_lenth = random.randint(2, 10)
numbers = [random.randint(0, 10) for i in range(list_lenth)]

print ("Исходный список элементов:")
print (numbers)
print ("Произведение пар:")
print(pairs_multiply(numbers))
