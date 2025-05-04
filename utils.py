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

def maximais_minimais(matriz: np.array) -> typing.Tuple[typing.List[int], typing.List[int]]:
    '''
    Encontramos os elementos maximais e minimais em uma relação representada por uma matriz.
    Elementos maximais: aqueles que não têm nenhum outro maior.
    Elementos minimais: aqueles que não têm nenhum outro menor.
    
    Args:
        matriz: Numpy.Array([]) - Matriz binária representando a relação.
        
    Returns:
        maximais: Lista de índices dos elementos maximais.
        minimais: Lista de índices dos elementos minimais.
    '''
    n = matriz.shape[0]  # Dimensão da matriz
    maximais = []
    minimais = []
    
    for i in range(n):
        # Elemento maximal: não existe nenhum outro elemento maior (não há 1 na linha do elemento para outro elemento)
        if np.all(matriz[i, :] == 0) and np.all(matriz[:, i] == 0):
            maximais.append(i)
        
        # Elemento minimal: não existe nenhum outro elemento menor (não há 1 na coluna do elemento para outro elemento)
        if np.all(matriz[:, i] == 0) and np.all(matriz[i, :] == 0):
            minimais.append(i)
    
    return maximais, minimais


def maior_menor_elemento(matriz: np.array) -> typing.Tuple[int, int]:
    '''
    Encontramos o maior e o menor elemento em uma relação representada por uma matriz.
    O maior elemento é aquele que é maior ou igual a todos os outros.
    O menor elemento é aquele que é menor ou igual a todos os outros.
    
    Args:
        matriz: Numpy.Array([]) - Matriz binária representando a relação.
        
    Returns:
        maior: Índice do maior elemento, se existir.
        menor: Índice do menor elemento, se existir.
    '''
    n = matriz.shape[0]  # Dimensão da matriz
    maior = None
    menor = None
    
    # O maior elemento é aquele que não tem nenhum elemento maior que ele (em todas as linhas e colunas)
    for i in range(n):
        if np.all(matriz[i, :] == 1) and np.all(matriz[:, i] == 1):
            maior = i
            break
    
    # O menor elemento é aquele que não tem nenhum elemento menor que ele (em todas as linhas e colunas)
    for i in range(n):
        if np.all(matriz[i, :] == 0) and np.all(matriz[:, i] == 0):
            menor = i
            break
    
    return maior, menor
