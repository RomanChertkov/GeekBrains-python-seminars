"""
Программа для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
для всех значений предикат.(0,0,0), (0,0,1) и тд.
"""
import os
os.system('clear')
PREDICAT_VALUES = [
    (0,0,0),
    (0,0,1),
    (0,1,0),
    (0,1,1),
    (1,0,0),
    (1,0,1),
    (1,1,0),
    (1,1,1)
]

def check_statement(predicat: tuple) -> None:
    """Сhecking a logical statement"""
    print(f"Для ({predicat[0]},{predicat[1]},{predicat[2]})")

    left_action_1 = bool(predicat[0]) or bool(predicat[1])
    left_action_2 = left_action_1 or predicat[2]
    left_side_result = not  left_action_2

    right_action_1 = not bool(predicat[0])
    right_action_2 = not bool(predicat[1])
    right_action_3 = not bool(predicat[2])
    right_action_4 = right_action_1 and right_action_2
    right_side_result = right_action_4 and right_action_3


    print("X ⋁ Y = ", left_action_1)
    print("(X ⋁ Y)⋁ Z = ",left_action_2)
    print("========================")
    print("Левая часть","¬(X ⋁ Y⋁ Z) = ",left_side_result)
    print("========================")
    print("¬X = ", right_action_1 )
    print("¬Y = ", right_action_2)
    print("¬Z = ", right_action_3)
    print("¬X ⋀ ¬Y = ", right_action_4)
    print("========================")
    print("Правая часть","¬X ⋀ ¬Y ⋀ ¬Z = ", right_side_result)
    print("========================")
    print("************************")

    if left_side_result == right_side_result:
        print(
            f"Для ({predicat[0]},{predicat[1]},{predicat[2]})",
            "утверждение верно"
        )
    else:
        print(
            f"Для ({predicat[0]},{predicat[1]},{predicat[2]})",
            "утверждение не верно"
        )
    print("*************************\n\n")


for item in PREDICAT_VALUES:
    check_statement(item)
