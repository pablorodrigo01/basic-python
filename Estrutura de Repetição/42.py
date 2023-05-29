# 42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

intervalos = {
    "[0-25]": 0,
    "[26-50]": 0,
    "[51-75]": 0,
    "[76-100]": 0
}

while True:
    numero = float(input("Digite um número positivo (ou um número negativo para sair): "))
    
    if numero < 0:
        break
    
    if numero >= 0 and numero <= 25:
        intervalos["[0-25]"] += 1
    elif numero >= 26 and numero <= 50:
        intervalos["[26-50]"] += 1
    elif numero >= 51 and numero <= 75:
        intervalos["[51-75]"] += 1
    elif numero >= 76 and numero <= 100:
        intervalos["[76-100]"] += 1

print("\nQuantidade de números nos intervalos:")
for intervalo, quantidade in intervalos.items():
    print(f"{intervalo}: {quantidade}")
