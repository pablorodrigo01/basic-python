# 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

l1 = float(input("Digite o primeiro lado do triangulo: "))
l2 = float(input("Digite o segundo lado do triangulo: "))
l3 = float(input("Digite o tercerio lado do triangulo: "))

if l1 == l2 == l3:
    print("Triângulo Equilátero")
elif l1 == l2 or l2 == l3:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")