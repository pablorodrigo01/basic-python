# 7. Faça um programa que leia 5 números e informe o maior número.
ns = []

for i in range(5):
    n = float(input("Digite um número: "))
    ns.append(n)

maior = max(ns)

# Exibir o resultado
print("O maior número é:", maior)
