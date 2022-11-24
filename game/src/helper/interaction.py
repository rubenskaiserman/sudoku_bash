def imprime_linha(LINHA_STRING:str):
    length = len(LINHA_STRING)
    for j in range(length):
        if (j + 1) % 9 == 0:
            print(j)
        elif (j + 1) % 3 == 0:
            print(j, end=' || ')
        else:
            print(j, end=' | ')

def imprime_divisor(i:int):
    if (i + 1) % 3 == 0 and (i + 1) % 9 != 0:
        print('- '*18)
    elif (i + 1) % 3 != 0:
        print('= '* 18)

def imprime(T: list[list]):
    for i in range(len(T)):
        imprime_linha(T[i])
        imprime_divisor(i)
        

def verifica_posicao_fixa(F, L, C):
    return (L, C) in F

def marca(T, L, C, V):
    if verifica_posicao_fixa(T, L, C):
        T[L][C] = V
        return True
    else:
        return False

