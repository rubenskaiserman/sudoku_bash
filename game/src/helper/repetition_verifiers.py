def get_regioes(T:list[list])->dict:
    # Separa as regiões do tabuleiro
    regioes = {
        "R1": T[0][0:3] + T[1][0:3] + T[2][0:3],
        "R2": T[0][3:6] + T[1][3:6] + T[2][3:6],
        "R3": T[0][6:] + T[1][6:] + T[2][6:],
        "R4": T[3][0:3] + T[4][0:3] + T[5][0:3],
        "R5": T[3][3:6] + T[4][3:6] + T[5][3:6],
        "R6": T[3][6:] + T[4][6:] + T[5][6:],
        "R7": T[6][0:3] + T[7][0:3] + T[8][0:3],
        "R8": T[6][3:6] + T[7][3:6] + T[8][3:6],
        "R9": T[6][6:] + T[7][6:] + T[8][6:],
    }
    return regioes


def verifica_regiao(T:list, R:str)->bool:
    # Verifica se a região está com valores repetidos
    regioes = get_regioes(T)

    regiao = regioes[R]
    for item in regiao:
        if regiao.count(item) > 1: return False
    return True

def verifica_coluna(T:list[list], C:int)->bool:
    # verifica se a coluna está com valores repetidos
    coluna = []
    for row in range(9):
        coluna.append(T[row][C])
    
    for item in coluna:
        if coluna.count(item) > 1: return False
    return True

def verifica_linha(T: list[list], L:int)->bool:
    # Verifica se a linha está com valores repetidos
    for item in T[L]:
        if T[L].count(item) > 1: return False 
    return True

def position_group(position:tuple)->str:
    # Verifica o grupo de uma determinada posição
    if position[0] < 3 and position[1] < 3:
        group = 'R1'
    elif position[0] < 3 and position[1] < 6:
        group = 'R2'
    elif position[0] < 3:
        group = 'R3'
    elif position[0] < 6 and position[1] < 3:
        group = 'R4'
    elif position[0] < 6 and position[1] < 6:
        group = 'R5'
    elif position[0] < 6:
        group = 'R6'
    elif position[1] < 3:
        group = 'R7'
    elif position[1] < 6:
        group = 'R8'
    else:
        group = 'R9'
    
    return group

def get_value_positions(T:list[list])->dict:
    # Retorna todas as posições que um determinado valor se encontra
    POSSIBLE_VALUES = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    T_LENGTH = len(T)
    LINE_LENGTH = len(T[0])
    value_positions = dict()

    for value in POSSIBLE_VALUES:
        value_positions[value] = []
        for i in range(T_LENGTH):
            for j in range(LINE_LENGTH):
                if T[i][j] == value:
                    value_positions[value].append((i, j))

    return value_positions

def verifica_conflito(T:list[list])->dict:
    # Retorna posições em conflito
    VALUE_POSITIONS = get_value_positions(T)
    conflitos = dict()

    for key, positions in VALUE_POSITIONS.items():
        conflitos[key] = []
        for line, column in positions:
            for line_j, column_j in positions:
                if ((line == line_j or column == column_j) or (position_group((line, column)) == position_group((line_j, column_j)))) and (line, column) != (line_j, column_j) and (line_j, column_j) not in conflitos[key]:
                    if (line, column) not in conflitos[key]:
                        conflitos[key].append([line, column])
                    conflitos[key].append([line_j, column_j])
    
    return conflitos

def verifica_tabuleiro(T):
    # Verifica se o tabuleiro está preenchido. Se sim, verifica se está correto
    # Se correto entrega uma mensagem de parabéns
    # Se incorreto informa as posições de conflito
    end_game = True
    for line in T:
        if line.count('0') > 0:
            end_game = False
            return end_game

    for i in range(len(T)):
        if verifica_linha(T, i):
            conflitos = verifica_conflito(T)
            for key, positions in conflitos.items():
                if positions != []:
                    print(f'Valor {key} existe nas posições: {positions}')
                    end_game = False
                    return end_game
            
    for i in range(len(T[0])):
        if verifica_coluna(T, i):
            conflitos = verifica_conflito(T)
            for key, positions in conflitos.items():
                if positions != []:
                    print(f'Valor {key} existe nas posições: {positions}')
                    end_game = False
                    return end_game

    for i in range(9):
        if verifica_regiao(T, f'R{i + 1}'):
            conflitos = verifica_conflito(T)
            for key, positions in conflitos.items():
                if positions != []:
                    print(f'Valor {key} existe nas posições: {positions}')
                    end_game = False
                    return end_game
    if end_game:
        print('PARABÉNS! BOM JOGO')
    return end_game
    