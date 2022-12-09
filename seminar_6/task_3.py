"""
Напишите программу, которая принимает на вход вещественное число
и показывает сумму его цифр.
- 6782 -> 23
- 0,56 -> 11
"""

import os

os.system("clear")

numbers = [ int(i) for i in input("Введите число: ") if i.isdigit() ]

print("Сумма цифр числа = ",sum(numbers))
