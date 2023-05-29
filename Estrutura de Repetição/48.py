# 48. Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido

numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero < 0:
    print("O número deve ser positivo.")
else:
    numero_invertido = int(str(numero)[::-1])
    print("Número invertido:", numero_invertido)