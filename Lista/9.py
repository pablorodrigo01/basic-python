# 9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

A = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    A.append(numero)

soma_quadrados = sum([num**2 for num in A])

print(f"A soma dos quadrados dos elementos do vetor A é: {soma_quadrados}")
