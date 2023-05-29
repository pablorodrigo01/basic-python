# 49. Faça um programa que mostre os n termos da Série a seguir: S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. Imprima no final a soma da série.

n = int(input("Digite a quantidade de termos da série: "))

soma = 0.0
m = 1

for i in range(1, n+1):
    termo = i / m
    soma += termo
    print(f"{i}/{m} = {termo}")
    m += 2

print("Soma da série:", soma)
