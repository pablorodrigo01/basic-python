# 21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Digite um número inteiro: "))

# Verifica se o número é menor que 2
if num < 2:
    print("Não é um número primo.")
    exit()

# Percorre os possíveis divisores do número até a sua metade
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print("Não é um número primo.")
        break
else:
    print("É um número primo.")
