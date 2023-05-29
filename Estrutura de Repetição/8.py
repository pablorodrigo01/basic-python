# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

ns = []
soma = 0

for i in range(5):
    n = float(input("Digite um número: "))
    ns.append(n)
    soma += n

media = soma / 5

# Exibir o resultado
print("A soma dos números é:", soma)
print("A média dos números é:", media)
