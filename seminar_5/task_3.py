"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные данные хранятся в отдельных текстовых файлах.
"""
import os

def compress_string(string:str)->str:
    """Compress input string"""
    output_string=''
    current_char = string[0]
    prev_char = ''
    count = 0
    for i in string:
        if current_char == i:
            count+=1
            prev_char = i
        else:
            current_char = i
            output_string += str(count)+prev_char
            count= 1
    output_string += str(count)+prev_char

    return output_string

def decompress_string(string:str)->str:
    """Decompress input string"""
    output_string=''

    char_count = ''
    for i in string:
        if i.isdigit():
            char_count+=i
        else:
            output_string+=i*int(char_count)
            char_count=''
    return output_string

os.system('clear')

with open("task_3_input_for_comress.txt",'r',encoding='UTF-8') as f1:
    input_for_compress = f1.readline()

with open("task_3_input_for_decomress.txt",'r', encoding='UTF-8') as f2:
    input_for_decompress = f2.readline()

with open("task_3_out_comress.txt",'w', encoding='UTF-8') as output_compress:
    output_compress.write(compress_string(input_for_compress))

with open("task_3_out_decomress.txt",'w', encoding='UTF-8') as output_decompress:
    output_decompress.write(decompress_string(input_for_decompress))



compress_string(input_for_compress)
decompress_string(input_for_decompress)
