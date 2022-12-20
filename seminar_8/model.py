"""
App model
"""
import json

def get_db()-> dict:
    """read data from db"""
    
    with open("students_db.json","r", encoding="UTF-8") as file:
        data = json.load(file)
    return data

def save_to_db(data: dict)-> None:
    """write data to db"""
    with open("students_db.json","w", encoding="UTF-8") as file:
        json.dump(data, file)

def add_student(student:list)->None:
    """Add student info in db"""
    students  = get_db()

    students[student[0]] = [student[1], student[2],{}]
    save_to_db(students)

def is_student_exist(lastname)->bool:
    """Is student in db?"""
    students  = get_db()
    return bool(students.get(lastname))

def add_student_evaluations(student_lastname:str, evaluations:list )->None:
    """Save student evaluations in db"""
    students  = get_db()
    students[student_lastname][2][evaluations[0]] = evaluations[1]

    save_to_db(students)

def get_student_info(lastname:str)->list:
    """Find students info in db"""
    students  = get_db()
    return students[lastname]
