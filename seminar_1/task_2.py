"""
Программа принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).
"""

def find_quater(coord_x:int , coord_y:int) -> int:
    """Find coord quater"""
    if coord_x>0 and coord_y>0 :
        return 1
    elif coord_x<0 and coord_y>0 :
        return 2
    elif coord_x<0 and coord_y<0 :
        return 3
    elif coord_x>0 and coord_y<0 :
        return 4


point = (
    int(input("Введите координату X\n")),
    int(input("Введите координату Y\n"))
    )

if point[0]== 0 and point[1] == 0:
    print("Координаты не должны быть = 0")

print(
    "Точка принадлежит",
    find_quater(point[0], point[1]),
    "координатной четверти"
)
