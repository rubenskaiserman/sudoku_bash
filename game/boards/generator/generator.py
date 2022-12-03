from random import randint
import sys
sys.path.append('./game/')
from src.helper.repetition_verifiers import *

for i in range(50):
    print(i)
    board = []
    for j in range(9):
        board.append([])
        for k in range(9):
            board[j].append('0')

    j = 0
    while j < 30:   
        random_line = randint(0, 8)
        random_column = randint(0, 8)
        random_value = randint(1, 9)
        board[random_line][random_column] = str(random_value)
        for line in board:
            print(line)
        if ((not verifica_linha(board, random_line)) or (not verifica_coluna(board, random_column)) or (not verifica_regiao(board, position_group((random_line, random_column))))):
            board[random_line][random_column] = '0'
        else:
            j += 1

    board_text = ''
    for line in board:
        board_text += ' , '.join(line)
        board_text += '\n'

    with open(f'./game/boards/board{i}.csv', 'w') as file:
        file.write(board_text)


