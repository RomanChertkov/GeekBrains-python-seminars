"""
Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу
между максимальным и минимальным значением дробной части элементов.
"""

import os
import random

os.system('clear')


list_lenth = random.randint(2, 10)
numbers = [round(random.uniform(1, 10),2) for i in range(list_lenth)]

fractional_part = [round(f % 1,2) for f in numbers]
min_element = min(fractional_part)
max_element = max(fractional_part)

print ("Исходный список элементов:")
print (numbers)
print(f"max = {max_element}, min  = {min_element}")
print(f"max - min = {round(max_element-min_element,2)} ")
