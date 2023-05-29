# 24. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

def lancar_dado():
    return random.randint(1, 6)

num_lancamentos = 100
resultados = []

for _ in range(num_lancamentos):
    resultado = lancar_dado()
    resultados.append(resultado)

contagem = [0] * 6

for resultado in resultados:
    contagem[resultado - 1] += 1

for i, quantidade in enumerate(contagem, start=1):
    print(f"Número {i} foi conseguido {quantidade} vezes.")
