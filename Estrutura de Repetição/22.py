# 22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Digite um número inteiro: "))

# Verifica se o número é menor que 2
if num < 2:
    print("Não é um número primo.")
    exit()

divisores = []  # Lista para armazenar os divisores do número

# Percorre os possíveis divisores do número até a sua metade
for i in range(2, num // 2 + 1):
    if num % i == 0:
        divisores.append(i)

if len(divisores) == 0:
    print("É um número primo.")
else:
    print("Não é um número primo. É divisível por:", divisores)