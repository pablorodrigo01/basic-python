# 18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n1 = int(input("Digite a quantia de numeros: "))

ns = []
for i in range(n1):
    c = float(input("Digite um numero: "))
    ns.append(c)

menor = min(ns)
maior = max(ns)
soma = sum(ns)

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Soma dos valores:", soma)