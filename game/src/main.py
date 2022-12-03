from helper import board_builder, interaction, repetition_verifiers
from random import randint

def inicia_jogo()->None:
    # Função main do jogo
    file_id = randint(0, 49)
    file_dir = f'../boards/board{file_id}.csv'
    board_file = board_builder.le_sudoku(file_dir)
    board = board_builder.cria_tabuleiro(board_file)
    posicoes_fixas = board_builder.armazena_posicoes_fixas(board_file)
    while not repetition_verifiers.verifica_tabuleiro(board):
        print('\n'*20)
        interaction.imprime(board)
        print('\n'*2)
        insertion = input('Escolha uma posição [X, Y] e um valor: ').replace('[', '').replace(']', '').split(', ')
        position = [int(insertion[0]), int(insertion[1])]
        value = insertion[2]
        if 0 <= position[0] <= 8 and 0 <= position[1] <= 8 and 1 <= int(value) <= 9 :
            if not interaction.verifica_posicao_fixa(posicoes_fixas, position[0], position[1]):
                board_file = interaction.marca(board_file, position[0], position[1], value)
                board = board_builder.cria_tabuleiro(board_file)  
            else:
                print("Posição fixa! Escolha outra.")
        else:
            print("Indice Inválido")  



if __name__ == '__main__':
    inicia_jogo()