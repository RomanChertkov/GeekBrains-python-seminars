"""
Создайте программу для игры с конфетами человек против бота.
Условие задачи: На столе лежит 120 конфета.
Играют два игрока делая ход друг после друга.
Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
Победитель - тот, кто оставил на столе 0 конфет.
"""

import os
import random
MAX_CANDIES_PER_MOVE = 28

def human_move(candies:int)->int:
    """human_move"""
    move = int(input("Сколько конфет Вы возьмёте? "))
  
    while not (move > 1 and move <= MAX_CANDIES_PER_MOVE):
        print(f"Ошибка! Можно взять максимум {MAX_CANDIES_PER_MOVE} конфет" )
        move = int(input("Сколько конфет Вы возьмёте? "))
    candies-=move
    print(f"Конфет осталось {candies}")
    return candies

def bot_move(candies:int)->int:
    """bot_move"""
    if candies< MAX_CANDIES_PER_MOVE:
        move = candies
    else:
        move = random.randint(1,28)
    candies-=move
    print(f"Бот взял {move}")
    print(f"Конфет осталось {candies}")
    return candies

os.system('clear')
total_candies = 120


while True:
    total_candies = human_move(total_candies)
    if total_candies == 0:
        print("Вы выиграли у бота")
        break

    total_candies = bot_move(total_candies)
    if total_candies == 0:
        print("Бот Вас победил")
        break
