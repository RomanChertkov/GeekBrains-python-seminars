"""
Создайте программу для игры с конфетами человек против умного бота.
Условие задачи: На столе лежит 120 конфета.
Играют два игрока делая ход друг после друга.
Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
Победитель - тот, кто оставил на столе 0 конфет.
"""


import os
total_candies = 120
MAX_CANDIES_PER_MOVE = 28

# Сумма ходов человека и бота на которую общее число конфет делится  без остатка
sum_of_moves =total_candies//(total_candies // MAX_CANDIES_PER_MOVE)
print(sum_of_moves)
def human_move(candies:int)->list[int]:
    """human_move"""
    move = int(input("Сколько конфет Вы возьмёте? "))

    while not (move >= 1 and move <= MAX_CANDIES_PER_MOVE):
        print(f"Ошибка! Можно взять максимум {MAX_CANDIES_PER_MOVE} конфет" )
        move = int(input("Сколько конфет Вы возьмёте? "))
    candies-=move
    print(f"Конфет осталось {candies}")
    return [candies, move]

def smart_bot_move(candies:int, opponent_move_value:int)->int:
    """bot_move"""
    if candies< MAX_CANDIES_PER_MOVE:
        move = candies
    else:
        if opponent_move_value == 1:
            move = MAX_CANDIES_PER_MOVE
        else:
            move = sum_of_moves - opponent_move_value
    candies-=move
    print(f"Бот взял {move}")
    print(f"Конфет осталось {candies}")
    return candies



os.system('clear')



while True:
    human_turn = human_move(total_candies)
    total_candies  = human_turn[0]
    human_move_value = human_turn[1]
    if total_candies == 0:
        print("Вы выиграли у бота")
        break

    total_candies = smart_bot_move(total_candies, human_move_value)
    if total_candies == 0:
        print("Бот Вас победил")
        break
