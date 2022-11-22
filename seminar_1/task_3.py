"""
Программа по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""

def print_quater_limits(quater_number:int) -> None:
    """Print coordinate quater limits"""
    match quater_number:
        case 1:
            print("В 1 четверти x>0 y>0 ")
        case 2:
            print("Во 2 четверти x<0 y>0 ")
        case 3:
            print("В 3 четверти x<0 y<0 ")
        case 4:
            print("В 4 четверти x>0 y<0 ")
        case _:
            print("Ошибка. Нет такой четверти")

print_quater_limits(int(input("Введите номер Координатной четверти: ")))
