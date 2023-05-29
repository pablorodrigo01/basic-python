# 50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos

n = int(input("Digite a quantidade de termos (N): "))

soma = 0.0

for i in range(1, n+1):
    termo = 1 / i
    soma += termo

print("Valor de H com", n, "termos:", soma)

