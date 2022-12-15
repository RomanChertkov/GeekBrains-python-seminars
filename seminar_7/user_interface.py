"""
App UI
"""

def choose_operation()->int:
    """Opeeration variants"""

    print("Для добавления человека в справочник нажмите 1")
    print("Для вывода всего справочника нажмите 2")
    variant =int(input("Выберите действие: "))

    return variant


def get_person_data()->list[str]:
    """Get data from console"""
    first_name = input("Введите фамилию: ")
    last_name = input("Введите  имя: ")
    phone_number = input("Введите телефон: ")
    item_description = input("Введите  описание: ")

    return [first_name, last_name, phone_number, item_description ]

def print_all_persons(data:list[str]):
    """Print all data to console"""
    if len(data) == 0:
        print("Справочние пуст :(")
    for i in data:
        person_data = i.split(', ')
        print(
            "Фамилия:",person_data[0],
            "Имя:",person_data[1],
            "телефон:",person_data[2],
            "описание: ",person_data[3],
            end=""
        )
