# 17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n1 = int(input("Digite um numero: "))

if n1 >= 0:
    f = 1
    for i in range(1, n1 + 1):
        f *= i

print(f) 