# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 <= n2 and n1 <= n3:
    maior = n1
elif n2 <= n1 and n2 <= n3:
    maior = n2
else:
    maior = n3

print("O menor número é:", maior)