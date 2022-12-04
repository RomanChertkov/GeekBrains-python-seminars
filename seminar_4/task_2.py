"""
Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N
"""

import os

def is_prime(number: int)-> bool:
    """ Check prime number"""
    for i in range(2, (number//2)+1):
        if number % i == 0:
            return False
    return True

def prime_multipliers(number: int)->list[int]:
    """Find prime multipliers of input number"""
    multipliers = []
    divider = 2
    while number!= 1:
        if number % divider == 0:
            multipliers.append(divider)
            number/=divider
        else:
            divider+=1
            while is_prime(divider) is False :
                divider+=1

    return multipliers


os.system('clear')

input_number = int(input("Введите натуральное число: "))

print("Простые множители числа:",*prime_multipliers(input_number))
