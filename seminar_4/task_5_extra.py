"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов
"""

import os

def generate_polynomial(ratios: list[int])-> str:
    """generate polynomial"""
    polynomial = ''
    lenth = len(ratios)

    for i in range(lenth):
        if i == 0:
            polynomial+= f"{ratios[i]}"
        elif i == 1:
            polynomial+=f" + {ratios[i]}*x"
        else:
            polynomial+=f" + {ratios[i]}*x^{i}"

    return polynomial

def convert_to_list(polinomial:str)->list[int]:
    """Convert polinomial from string to ratios list"""
    temp = polinomial.replace(" ","").split('+')
    polinomial_ratios = [0]*len(temp)
    for i in temp:

        if i.isdigit() is True:
            polinomial_ratios[0]= int(i)
        elif i[-2:] == '*x':
            polinomial_ratios[1] = int(i[:-2])
        else:
            element = i.split('*x^')
            polinomial_ratios[int(element[1])]= int(element[0])


    return polinomial_ratios


def polinomials_sum(polinomial1:list[int],polinomial2:list[int])->list[int]:
    """Polinomials sum"""

    lenght1 =len(polinomial1)
    lenght2 =len(polinomial2)

    if lenght1>lenght2:
        lenght = lenght1
        stop = lenght2
        result = polinomial1.copy()
    else:
        lenght = lenght2
        stop = lenght1
        result = polinomial2.copy()

    for i in range(lenght):
        if i>stop-1:
            break
        result[i] = polinomial1[i]+polinomial2[i]

    return result

os.system('clear')

file = open("task_5_file1.txt",'r')
polinomial_1 = file.readline()
file.close()

file = open("task_5_file2.txt", 'r')
polinomial_2 = file.readline()
file.close()

output = open("task_5_outputfile.txt",'w')
output.write(
    generate_polynomial(
        polinomials_sum(
            convert_to_list(polinomial_2),
            convert_to_list(polinomial_1)
        )
    )
)

output.close()
