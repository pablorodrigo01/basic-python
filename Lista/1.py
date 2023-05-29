# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os

def ler_vetor():
    vetor = []
    for i in range(5):
        n = int(input(f"Digite o número {i+1}: "))
        vetor.append(n)
    return vetor

def mostrar_vetor(vetor):
    print("Números digitados:")
    for n in vetor:
        print(n)

ns = ler_vetor()

mostrar_vetor(ns)
