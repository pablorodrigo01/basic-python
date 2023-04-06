# 15. Faça um Programa que peça os 3 ls de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os ls formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

l1 = float(input("Digite o primeiro lado do triangulo: "))
l2 = float(input("Digite o segundo lado do triangulo: "))
l3 = float(input("Digite o tercerio lado do triangulo: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 and l2 == l3:
        print("O triângulo é equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os valores informados não formam um triângulo.")
