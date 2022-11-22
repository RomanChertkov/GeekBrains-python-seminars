"""
Программу принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным
"""


def is_holiday(day_of_week: int)-> bool:
    """find holiday"""
    match day_of_week:
        case 1:
            return False
        case 2:
            return False
        case 3:
            return False
        case 4:
            return False
        case 5:
            return False
        case 6:
            return True
        case 7:
            return True
        case _:
            return False

def print_result(res: bool)-> None:
    """Print result"""
    if res :
        print("Выходной день")
    print("Будний день")

day_number = int(input("Введите номер дня недели: "))
print_result(is_holiday(day_number))
