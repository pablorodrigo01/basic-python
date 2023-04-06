# 17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("O ano", ano, "é bissexto.")
else:
    print("O ano", ano, "não é bissexto.")
