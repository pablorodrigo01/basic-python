# 1. Faça um programa para imprimir:
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = ""
        for j in range(i):
            linha += str(i) + " "
        print(linha)

def main():
    n = int(input("Digite o valor de N: "))
    imprimir_padrao(n)
