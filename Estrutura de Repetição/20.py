# 20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

n1 = int(input("Digite um numero: "))

if n1 >= 0:
    f = 1
    for i in range(1, n1 + 1):
        f *= i

print(f) 