"""
Программа находит наименьший натуральный делитель целого числа N, отличный от 1.
"""
import os

os.system('clear')

def min_devisor(number: int) -> int:
    """Minimal devisor"""

    if number == 1:
        return 1

    for i in range(2 ,number+1):
        if number % i == 0:
            return i

input_number = int(input("Введите число N: "))

print(
    "Наименьший натуральный делитель числа",
    input_number, "=",
    min_devisor(input_number)
)
