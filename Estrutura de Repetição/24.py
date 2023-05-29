# 24. Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input("Digite a quantidade de notas: "))

soma = 0

for i in range(n):
    nota = float(input("Digite a nota: "))
    soma += nota

media = soma / n

print("A média aritmética das notas é:", media)
