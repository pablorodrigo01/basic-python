# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("Digite o valor do primeiro produto: "))
p2 = float(input("Digite o valor do segundo produto: "))
p3 = float(input("Digite o valor do tercerio produto: "))

if p1 <= p2 and p1 <= p3:
    barato = p1
elif p2 <= p1 and p2 <= p3:
    barato = p2
else:
    barato = p3

print("O produto mais barato é: ", barato)
