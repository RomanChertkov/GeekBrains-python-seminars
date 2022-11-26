"""
Программа считает сумму чётных чисел,
расположенных между числами 1 и N включительно.
"""
import os

os.system('clear')

def evens_sum(number:int)->int:
    """evens numbers sum in range from 1 to number"""
    result_sum = 0
    for i in range(2, number+1, 2):
        result_sum+=i
    return result_sum

input_number = int(input("Введите число N: "))

print(
    "Cумма чётных чисел, расположенных между числами 1 и",
    input_number,
    "включительно =",
    evens_sum(input_number)
)
