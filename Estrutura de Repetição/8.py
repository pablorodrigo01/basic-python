# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []
soma = 0

for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)
    soma += numero

media = soma / 5

# Exibir o resultado
print("A soma dos números é:", soma)
print("A média dos números é:", media)
