def verifica_regiao(T, R):
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

    regiao = regioes[R]
    print(regiao)
    for item in regiao:
        if regiao.count(item) > 1: return False
    return True

def verifica_coluna(T, C):
    coluna = []
    for row in range(9):
        coluna.append(T[row][C])
    
    for item in coluna:
        if coluna.count(item) > 1: return False
    return True

def verifica_linha(T, L):
    for item in T[L]:
        if T[L].count(item) > 1: return False 
    return True