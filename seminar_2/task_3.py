"""
Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных ИНДЕКСАХ.
Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
"""

import os
import random

os.system('clear')

input_number = int(input("Введите число N: "))
indexes_lenth = random.randint(1, 2*input_number)


input_indexes = [
    random.randint(0, 2*input_number) for i in range(indexes_lenth)
]

input_numbers  = [item for item in range(-input_number,input_number+1)]

def list_items_multiply(numbers: list, indexes:list)->int:
    """list items multiply"""

    multiply = 1
    for item in indexes:
        multiply*=numbers[item]

    return multiply

res = list_items_multiply(input_numbers, input_indexes)

print ("indexes", input_indexes)
print ("numbers", input_numbers)
print ("Произведение элементов =", res)
