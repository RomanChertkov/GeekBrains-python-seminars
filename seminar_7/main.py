"""
Телефонный справочник
"""

import os
import user_interface as ui
import  file_operations as files
def main():
    """Entry point"""

    os.system('clear')
    variant = ui.choose_operation()

    if variant == 1:
        person_data = ui.get_person_data()
        files.export_person_col(person_data)
        files.export_person_row(person_data)
        print("Информация добавлена")
    elif variant == 2:
        all_people =  files.import_all_people()
        ui.print_all_persons(all_people)
    else:
        print("Ошибка! Такого варианта нет.")


if __name__ == "__main__":
    main()
