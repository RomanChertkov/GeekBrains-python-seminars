"""
Создайте программу для игры в ""Крестики-нолики"".
"""
import os


def print_board()->None:
    """Print play board to console"""
    print('\n ',*[0,1,2], sep="  ")
    rows=0
    for i in play_board:
        print(rows, end="  ")
        for j in i:
            print( j,  end='  ')
        rows+=1
        print()
    print()

def validate_move(cell_number:list[int])->bool:
    """ Validate user move"""
    if play_board[cell_number[0]][cell_number[1]] == '_':
        return True
    return False

def do_move(cell_number:list[int], char:str)->None:
    """Write user move"""
    play_board[cell_number[0]][cell_number[1]] = char

def ask_move(char: str)->list[int]:
    """Ask move"""
    return list(
        map(
            int,
            input(f'Игрок {char} введи индексы ячейки через пробел: ').split()
        )
    )

def is_winner(cell_number:list[int])->bool:
    """check winner"""
    char = play_board[cell_number[0]][cell_number[1]]
    
    return check_row(cell_number[0], char) \
        or check_col(cell_number[1], char) \
        or check_diagonals(cell_number,char)

def check_row(row:int, char: str)-> bool:
    """Check elements in row"""
    char_coincidence= 0

    for i in play_board[row]:
        if char == i:
            char_coincidence+=1

    return char_coincidence == 3

def check_col(col:int, char: str)-> bool:
    """Check elements in col"""
    char_coincidence= 0

    for i in play_board:
        if char == i[col]:
            char_coincidence+=1

    return char_coincidence == 3

def check_diagonals(cell_number:list[int], char)-> bool:
    """Check elements in diagonals"""
    if cell_number[0]==cell_number[1]:
        return check_main_diagonal(True,char)
    elif cell_number[0]==1 and cell_number[1]== 1:
        return check_main_diagonal(True,char) or check_main_diagonal(False,char)
    else:
        return  check_main_diagonal(False,char)


def check_main_diagonal(is_main:bool,char)->bool:
    """Check main  diagonal or other"""
    char_coincidence= 0
    if is_main:
        for i in range(3):
            if play_board[i][i] == char:
                char_coincidence+=1
    else:
        for i in range(3):
            if play_board[i][2-i] == char:
                char_coincidence+=1
    return char_coincidence == 3

os.system('clear')

play_board = [['_']*3,['_']*3,['_']*3]
PLAY = True
count=1

print_board()

while PLAY:
    player_char = 'X' if count%2 else 'O'
    move = ask_move(player_char)
    while not validate_move(move):
        print("Ошибка! Эта ячейка уже отмечена.")
        move = ask_move(player_char)

    do_move(move,player_char)

    print_board()

    if is_winner(move):
        print(f"Игрок {player_char} победил! Поздравляю!")
        break

    count+=1
