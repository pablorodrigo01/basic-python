# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n = float(input("Digite um número: "))

if n > 0:
    print("O número é positivo:", n)
elif n < 0:
    print("O maior é negativo:", n)
else:
    print("O número é igual a zero")
