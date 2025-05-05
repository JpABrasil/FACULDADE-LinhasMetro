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

def maximais_minimais(matriz: np.array):
    n = matriz.shape[0]
    maximais = []
    minimais = []

    for i in range(n):
        # Verifica se a linha i é toda 0 (exceto diagonal)
        if all(matriz[i][j] == 0 for j in range(n) if j != i):
            maximais.append(i)

        # Verifica se a coluna i é toda 0 (exceto diagonal)
        # e se matriz[i][i] == 1 (tem laço reflexivo)
        if matriz[i][i] == 1 and all(matriz[j][i] == 0 for j in range(n) if j != i):
            minimais.append(i)

    return maximais, minimais



def maior_menor_elemento(matriz: np.array):
    n = matriz.shape[0]
    maior = None
    menor = None

    for i in range(n):
        # Verifica se linha i é toda 1 (com exceção de matriz[i][i])
        if all(matriz[i][j] == 1 or j == i for j in range(n)):
            maior = i

        # Verifica se coluna i é toda 1 (com exceção de matriz[i][i])
        if all(matriz[j][i] == 1 or j == i for j in range(n)):
            menor = i

    return maior, menor

def composicao_relacoes(metro: np.array, onibus: np.array) -> np.array:
    '''
    Faz a composição entre a matriz do metrô e do ônibus,
    sair de uma estacao de metro, pegar um onibus e chegar em outra estacao.


    A composição representa: se existe i -> j no metrô e j -> k no ônibus,
    então existe i → k na composição.

    Args:
        metro: Numpy.Array([]) representando a matriz de adjacência do metrô
        onibus: Numpy.Array([]) representando a matriz de adjacência do ônibus

    Returns:
        matriz_resultante: Numpy.Array([]) com a composição (metrô seguido de ônibus)
    '''
    n = metro.shape[0]
    matriz_resultante = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if metro[i][k] == 1 and onibus[k][j] == 1:
                    matriz_resultante[i][j] = 1
    return matriz_resultante

