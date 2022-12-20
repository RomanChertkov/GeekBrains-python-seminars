"""
App entry point
"""
import os
import user_interface as ui
import model

def main():
    """Entry point"""
    os.system("clear")

    if ui.get_user_type() == 1 :
        if ui.get_adding_type() == 1:
            while True:
                model.add_student(ui.ask_student_info())
                if not ui.repeat_current_operation():
                    break
        else:
            while True:
                model.add_student_evaluations(
                    validate_user(),
                    ui.ask_evaluations()
                )
                if not ui.repeat_current_operation():
                    break
    else:
        while True:
            ui.show_student_info(model.get_student_info(validate_user()))
            if not ui.repeat_current_operation():
                break

def validate_user()->str:
    """Validate user"""
    lastname = ui.ask_student_lastname()
    while not model.is_student_exist(lastname):
        print("В базе нет такого ученика.")
        lastname = ui.ask_student_lastname()
    return lastname

if __name__== "__main__":
    main()
