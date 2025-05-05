import numpy as np
import typing

def reflexiva(matriz: np.array) -> typing.Tuple[bool, typing.Optional[np.array]]:
    '''
    Verificamos se todos os elementos da diagonal matriz são iguais a 1
    Args:
        matriz: Numpy.Array([])
    Returns:
        reflexiva: boolean
    '''
    if np.all(np.diag(matriz) == 1):
        return True, None
    else:
        fecho = matriz.copy()
        np.fill_diagonal(fecho, 1)
        return False, fecho

def simetrica(matriz: np.array) -> typing.Tuple[bool, typing.Optional[np.array]]:
    '''
    Verificamos se a matriz é igual a sua transposta
    Args:
        matriz: Numpy.Array([])
    Returns:
        simetrica: boolean
    '''
    if np.array_equal(matriz, matriz.T):
        return True, None
    else:
        fecho = matriz | matriz.T
        return False, fecho

def assimetrica(matriz: np.array) -> typing.Tuple[bool, None]:
    '''
    Verificamos para todo par de estações (i,j) se existe uma conexão de i para j,
    então não deve poder existir uma conexão de j para i.
    Fazemos isso verificando se o produto da matriz e sua transposta tem todos os elementos iguais a 0 e se a diagonal é igual a 0
    Args:
        matriz: Numpy.Array([])
    Returns:
        assimetrica: boolean
    '''
    return np.all((matriz * matriz.T) == 0) and np.all(np.diag(matriz) == 0), None

def antissimetrica(matriz: np.array) -> typing.Tuple[bool, None]:
    '''
    Isolamos a diagonal da matriz e comparamos em quais pares de posições na matriz original
    e na matriz transposta temos elementos iguais 1.
    Se houver algum caso em que (a,b) e
    (b,a) existem nas duas matrizes (original e transposta) retornamos falso
    Args:
        matriz: Numpy.Array([])
    Returns:
        antissimetrica: boolean
    '''
    n = matriz.shape[0] #Pegar dimensão da matriz
    off_diagonal = ~np.eye(n, dtype=bool) #Criar matriz com diagonal igual a 0 e outros elementos iguais a 1
    conflito = (matriz == 1) & (matriz.T == 1) & off_diagonal
    return not np.any(conflito), None

def transitiva(matriz: np.array) -> typing.Tuple[bool, typing.Optional[np.array]]:
    '''
    Realizamos o produto booleano da matriz com ela mesma, simulando sua composição de relações.
    Esse produto nos indica se há um caminho indireto na matriz original de i -> k.
    Depois verificamos se a matriz original contém a realçao i -> k. Caso não contenha retornamos falso
    '''
    m2 = (matriz @ matriz) > 0  # Produto booleano
    if np.all(m2 <= matriz):
        return True, None
    else:
        # Calcula o fecho transitivo usando o algoritmo de Warshall
        n = matriz.shape[0]
        fecho = matriz.copy()
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    fecho[i][j] = fecho[i][j] or (fecho[i][k] and fecho[k][j])
        return False, fecho

def equivalencia(matriz: np.array) -> bool:
    t = transitiva(matriz)[0]
    s = simetrica(matriz)[0]
    r = reflexiva(matriz)[0]
    if (t and r and s):
        return True
    return False

def ordem(matriz: np.array) -> bool:
    a = antissimetrica(matriz)[0]
    t = transitiva(matriz)[0]
    r = reflexiva(matriz)[0]
    if(a and t and r):
        return True
    return False


def maximais_minimais(matriz):
    maximais = []
    minimais = []

    if reflexiva(matriz)[0] and transitiva(matriz)[0] and antissimetrica(matriz)[0]:
        for i in range(len(matriz)):
            # Verifica se a linha i é zero (exceto a diagonal)
            if all(matriz[i][j] == 0 for j in range(len(matriz[0])) if j != i):
                maximais.append(i)
            # Verifica se a coluna i é zero (exceto a diagonal)
            if all(matriz[j][i] == 0 for j in range(len(matriz)) if j != i):
                minimais.append(i)
        print("Elementos maximal:", maximais)
        print("Elementos minimal:", minimais)
    else:
        print("A matriz não atende os requisitos de maximais e minimais.")

    return maximais, minimais


def maior_menor_elemento(matriz):
    linhas_maior_elemento = []
    linhas_menor_elemento = []

    for i in range(len(matriz)):
        if all(matriz[i]) and np.count_nonzero(matriz[i] == 1) == len(matriz[i]):
            linhas_maior_elemento.append(i)
        elif np.count_nonzero(matriz[i] == 1) == 1:
            linhas_menor_elemento.append(i)

    print("Maior: ", linhas_menor_elemento)
    print("Menor: ", linhas_maior_elemento)

    return linhas_menor_elemento, linhas_maior_elemento




def composicao_relacoes(metro, onibus):
    composicao = []

    for i in range(len(metro)):
        linha_composta = []
        for j in range(len(metro[0])):
            if metro[i][j] == 1 or onibus[i][j] == 1:
                linha_composta.append(1)
            else:
                linha_composta.append(0)
        composicao.append(linha_composta)

    return composicao
