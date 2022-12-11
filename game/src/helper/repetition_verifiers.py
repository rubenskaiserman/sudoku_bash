def get_regioes(T):
    length = len(T)
    regioes = {}
    chunck = int(length ** (1/2))
    regiao = 0
    starter = 0
    while regiao < length:
        for i in range(0, length, chunck):
            current_region = []
            for j in range(starter, starter + chunck):
                current_region += T[j][i: i + chunck]
            regioes[f'R{regiao + 1}'] = current_region
            regiao += 1
        starter += chunck
    
    return regioes

def verifica_regiao(T:list, R:str)->bool:
    # Verifica se a região está com valores repetidos
    # Tem valores repetidos: False
    # Não tem valores repetidos: True
    regioes = get_regioes(T)

    regiao = regioes[R]
    for item in regiao:
        if regiao.count(item) > 1 and item != '0': return False
    return True

def verifica_coluna(T:list[list], C:int)->bool:
    # verifica se a coluna está com valores repetidos
    length = len(T)
    coluna = []
    for row in range(length):
        coluna.append(T[row][C])
    
    for item in coluna:
        if coluna.count(item) > 1 and item != '0': return False
    return True

def verifica_linha(T: list[list], L:int)->bool:
    # Verifica se a linha está com valores repetidos
    for item in T[L]:
        if T[L].count(item) > 1 and item != '0': return False 
    return True

def position_group(position:tuple, length)->str:
    # Verifica o grupo de uma determinada posição
    length_root = length ** (1/2)
    line_factor = 1
    group = 1
    while group <= length:
        column_factor = 1
        if position[0] < line_factor * length_root:
            while column_factor <= length_root:
                if position[1] < column_factor * length_root:
                    return f'R{group}'
                else: 
                    group += 1
                    column_factor += 1
        else:
            line_factor += 1
            group += int(length_root)

def get_value_positions(T:list[list])->dict:
    # Retorna todas as posições que um determinado valor se encontra
    POSSIBLE_VALUES = range(len(T))
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
                if ((line == line_j or column == column_j) or (position_group((line, column), len(T)) == position_group((line_j, column_j), len(T)))) and (line, column) != (line_j, column_j) and (line_j, column_j) not in conflitos[key]:
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

    for i in range(len(T)):
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
    