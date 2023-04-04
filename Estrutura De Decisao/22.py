# 22. Faça um Programa que peça um n inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

n = int(input("Digite um número inteiro: "))

if n % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
