# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def ler_notas():
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    return notas

def mostrar_notas_e_media(notas, media):
    print("Notas:")
    for nota in notas:
        print(nota)
    print("Média:", media)

notas = ler_notas()

media = calcular_media(notas)

mostrar_notas_e_media(notas, media)
