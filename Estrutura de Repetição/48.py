# 48. Faça um programa que peça um n inteiro positivo e em seguida mostre este n invertido

n = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if n < 0:
    print("O número deve ser positivo.")
else:
    n_invertido = int(str(n)[::-1])
    print("Número invertido:", n_invertido)