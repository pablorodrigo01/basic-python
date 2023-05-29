# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 <= n2:
    for n in range(n1, n2 + 1):
        print(n)
else:
    for n in range(n1, n2 - 1, -1):
        print(n)
