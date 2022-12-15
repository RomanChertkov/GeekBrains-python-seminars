"""
Export/import data to file
"""

def import_all_people()->list[str]:
    "Import all peaple data from text file"
    peoples = []
    
    with open("db_row.txt","r", encoding="UTF-8") as app_db:
        for i in app_db:
            peoples.append(i)
    return peoples

def export_person_row(data:list[str])->None:
    "Export person data to text file in row"
    with open('db_row.txt', "a", encoding="UTF-8") as file:
        file.write(", ".join(data))
        file.write("\n")

def export_person_col(data:list[str])->None:
    "Export person data to text file in col"
    with open('db_col.txt', "a", encoding="UTF-8") as file:
        for i in data:
            file.write(f"{i}\n")
        file.write("\n")
