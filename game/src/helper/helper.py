def le_sudoku(arquivo:str)->str:
    # TODO: Montar error handlers

    with open(arquivo) as file:
        return file.read()

def cria_tabuleiro(conteudo:str):
    CHUNCK_LENGTH = 9
    FORMATED_BOARD = conteudo.replace('\n', '').replace(' , ', '')
    j = 0
    board = []

    for i in range(CHUNCK_LENGTH, CHUNCK_LENGTH ** 2 + 1, CHUNCK_LENGTH):
        board.append(FORMATED_BOARD[j:i])
        j += CHUNCK_LENGTH
    
    return board

def armazena_posicoes_fixas(conteudo):
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
    # armazena_posicoes_fixas(le_sudoku('./boards/imagem1.csv'))
    pass