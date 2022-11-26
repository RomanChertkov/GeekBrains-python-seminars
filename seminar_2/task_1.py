"""
Программа принимает на вход число N
и выдает набор произведений чисел от 1 до N.
"""

import math
import os

os.system('clear')

number = int(input("Введите число N: "))

result = [math.factorial(i) for i in range(1,number +1)]

print(result)
