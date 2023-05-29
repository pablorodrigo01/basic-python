# 51. Faça um programa que mostre os n termos da Série a seguir: S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. Imprima no final a soma da série.

n = int(input("Digite a quantidade de termos (N): "))

soma = 0.0
numerador = 1
denominador = 1

for i in range(n):
    termo = numerador / denominador
    soma += termo
    numerador += 1
    denominador += 2
    print(termo)

print("Soma da série:", soma)
