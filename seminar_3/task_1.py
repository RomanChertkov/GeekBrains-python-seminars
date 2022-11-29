"""
Программа найдёт сумму элементов списка, стоящих на нечётной позиции.
"""
import os
import random

os.system('clear')

def el_on_odd_index_sum(input_list: list)->list:
    """Calculate sum of elements on odd indexes"""
    total_sum = 0
    odd_index_elements = []
    for i in range(1,len(input_list),2):
        total_sum+=input_list[i]
        odd_index_elements.append(input_list[i])

    return [total_sum,odd_index_elements]

list_lenth = random.randint(2, 10)
numbers = [random.randint(0, 10) for i in range(list_lenth)]
result = el_on_odd_index_sum(numbers)

print ("Исходный список элементов:")
print (numbers)
print ("На нечётных позициях элементы",end=' ')
print (*result[1], sep=", ", end='. ')
print(f"Ответ: {result[0]}")
