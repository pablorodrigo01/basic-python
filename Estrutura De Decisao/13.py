# 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido

n = int(input("Digite um número de 1 a 7: "))

if n == 1:
    print("Domingo")
elif n == 2:
    print("Segunda-feira")
elif n == 3:
    print("Terça-feira")
elif n == 4:
    print("Quarta-feira")
elif n == 5:
    print("Quinta-feira")
elif n == 6:
    print("Sexta-feira")
elif n == 7:
    print("Sábado")
else:
    print("Valor inválido")
