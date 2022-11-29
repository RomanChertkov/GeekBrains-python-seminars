"""
Задайте число.
Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.
"""

import os

os.system('clear')

def all_fibo_numbers(number:int)->list:
    """Calculate positive and nevative fibo numbers"""
    fibo = [1,1]
    nfibo = [1,-1]
    if number == 1:
        return [-1, 0, 1]
    elif number == 2:
        nfibo.reverse()
        return nfibo +[0]+ fibo

    for i in range(2, number):
        value = fibo[i-2]+fibo[i-1]
        nvalue = value if i % 2 == 0 else -1* value
        fibo.append(value)
        nfibo.append(nvalue)

    nfibo.reverse()
    return nfibo +[0]+ fibo


fibo_number = int(input("Введите число: "))
print(all_fibo_numbers(fibo_number))
