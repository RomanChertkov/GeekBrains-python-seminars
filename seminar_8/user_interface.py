"""
App ui
"""
def show_student_info(student_info:list)-> None:
    """print student info to console"""
    print("Имя: ", student_info[0])
    print("Класс: ", student_info[1])
    print("Оценки по предметам:")
    for key, value in student_info[2].items():
        print(f"{key}: ", *value)



def get_user_type()->int:
    """Get user type"""
    print("Тип пользователя:")
    print("1 - Учитель")
    print("2 - Ученик")
    valid_value = False
    user_type = 0
    while not valid_value:
        user_type = int(input("Выберите тип пользователя: "))
        if user_type == 1:
            break
        elif user_type == 2:
            break
        else:
            print("Ошибка! нет такого типа пользователя.")
    return user_type

def get_adding_type()->int:
    """Get adding type"""
    print("Что Вы хотите сделать?")
    print("1 - Добавить ученика")
    print("2 - Добавить оценку ученику")
    valid_value = False
    adding_type = 0
    while not valid_value:
        adding_type = int(input("Выберите действие: "))
        if adding_type == 1:
            break
        elif adding_type == 2:
            break
        else:
            print("Ошибка! нет такого действия.")
    return adding_type

def ask_student_info()->list[str]:
    """Enter student info"""
    return input("Введите Фамилию, имя, класс через пробел: ").split()

def ask_student_lastname()->str:
    """Ask student lastname"""
    return input("Введите Фамилию ученика: ")


def ask_evaluations()->list:
    """Ask subject evaluations"""
    subject = input("Введите предмет: ")
    evaluations = list(
        map(int, input("Введите оценки через пробел:").split())
    )
    return [subject, evaluations]

def repeat_current_operation()->bool:
    """Exit dialog"""
    print("Хотите повторить текущую операцию?")
    variant =input("1-Да 2-Выход")

    match variant:
        case "1":
            return True
        case "2":
            return False
        case _:
            return False
