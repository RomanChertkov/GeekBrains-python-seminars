"""
Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
(Вывод тех элементов, которые были без повторов)
"""
import os
import random


def unique_numbers(numbers:list[int])->list[int]:
    """Search unique numbers in list"""
    dictionary = {}
    unique = []

    for item in numbers:
        if dictionary.get(item) is None:
            dictionary[item] = 1
        else:
            dictionary[item] +=1

    for key, value in dictionary.items():
        if value == 1:
            unique.append(key)

    return unique


os.system('clear')

lenght = random.randint(1,10)
random_numbers = [random.randint(0,10) for i in range(lenght)]

print("Список из случайных чисел",random_numbers)
print("Уникальные элементы списка:", unique_numbers(random_numbers))
