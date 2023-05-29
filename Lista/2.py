# 2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

def ler_vetor():
    vetor = []
    for i in range(10):
        n = float(input(f"Digite o número {i+1}: "))
        vetor.append(n)
    return vetor

def mostrar_vetor_inverso(vetor):
    print("Números digitados (ordem inversa):")
    for i in range(len(vetor)-1, -1, -1):
        print(vetor[i])

ns = ler_vetor()

mostrar_vetor_inverso(ns)
