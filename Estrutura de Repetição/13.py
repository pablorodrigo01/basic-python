# Faça um programa que peça dois números, b e e, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

b = float(input("Digite a base: "))
e = int(input("Digite o expoente: "))

c = 1

if e >= 0:
    for i in range(e):
        c *= b
else:
    for i in range(-e):
        c /= b

print("O calculo é:", c)
