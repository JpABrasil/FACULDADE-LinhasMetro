import numpy as np
from utils  import *

matriz_adjacencia = np.array([
    [0, 1, 0, 0, 0, 0],  # Estação Avenida
    [1, 0, 1, 0, 0, 0],  # Estação Centro
    [0, 1, 0, 0, 0, 0],  # Estação Praça
    [0, 0, 0, 0, 0, 1],  # Estação Parque
    [0, 0, 0, 0, 0, 1],  # Estação Shopping
    [0, 1, 1, 0, 1, 0],  # Estação Terminal
])


# Testar a função reflexiva
reflexiva_result, reflexiva_fecho = reflexiva(matriz_adjacencia)
print(f"Reflexiva: {reflexiva_result}")
if reflexiva_fecho is not None:
    print("Fecho Reflexivo:")
    print(reflexiva_fecho)

# Testar a função simétrica
simetrica_result, simetrica_fecho = simetrica(matriz_adjacencia)
print(f"Simétrica: {simetrica_result}")
if simetrica_fecho is not None:
    print("Fecho Simétrico:")
    print(simetrica_fecho)

# Testar a função assimétrica
assimetrica_result, _ = assimetrica(matriz_adjacencia)
print(f"Assimétrica: {assimetrica_result}")

# Testar a função antissimétrica
antissimetrica_result, _ = antissimetrica(matriz_adjacencia)
print(f"Antissimétrica: {antissimetrica_result}")

# Testar a função transitiva
transitiva_result, transitiva_fecho = transitiva(matriz_adjacencia)
print(f"Transitiva: {transitiva_result}")
if transitiva_fecho is not None:
    print("Fecho Transitivo:")
    print(transitiva_fecho)

# Testar a função de equivalência
equivalencia_result = equivalencia(matriz_adjacencia)
print(f"Equivalência: {equivalencia_result}")

# Testar a função de ordem
ordem_result = ordem(matriz_adjacencia)
print(f"Ordem: {ordem_result}")

# Testar a função de máximos e mínimos
maximais, minimais = maximais_minimais(matriz_adjacencia)


# Testar a função maior e menor elemento
maior, menor = maior_menor_elemento(matriz_adjacencia)


matriz_onibus = np.array([
    [0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0],
])
# Testar a composição das relações (Metrô -> Ônibus)
composicao = composicao_relacoes(matriz_adjacencia, matriz_onibus)
print("Composição Metrô -> Ônibus:")
print(composicao)

