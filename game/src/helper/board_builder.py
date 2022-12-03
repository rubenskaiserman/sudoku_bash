def le_sudoku(arquivo:str)->str:
    with open(arquivo) as file:
        return file.read()

def cria_tabuleiro(conteudo:str)->list:
    CHUNCK_LENGTH = 9
    BOARD_STRING = conteudo.replace('\n', ' , ').split(' , ')
    j = 0
    board = []

    for i in range(CHUNCK_LENGTH, CHUNCK_LENGTH ** 2 + 1, CHUNCK_LENGTH):
        board.append(BOARD_STRING[j:i])
        j += CHUNCK_LENGTH
    
    return board

def armazena_posicoes_fixas(conteudo:str)->list:
    LINE_COLUMN_LENGTH = 9
    BOARD = cria_tabuleiro(conteudo)
    EMPTY_SPACE = '0'
    
    linhas_fixas = []
    for i in range(LINE_COLUMN_LENGTH):
        for j in range(LINE_COLUMN_LENGTH):
            if BOARD[i][j] != EMPTY_SPACE:
                linhas_fixas.append((i, j))

    return linhas_fixas

if __name__ == '__main__':
    print(cria_tabuleiro(le_sudoku('./boards/imagem1.csv')))