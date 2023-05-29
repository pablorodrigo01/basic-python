# 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

def contar_consoantes(caracteres):
    consoantes = []
    for char in caracteres:
        if char.isalpha() and char.lower() not in 'aeiou':
            consoantes.append(char)
    return consoantes, len(consoantes)

def ler_caracteres():
    caracteres = []
    for i in range(10):
        char = input(f"Digite o caractere {i+1}: ")
        caracteres.append(char)
    return caracteres

def mostrar_consoantes(consoantes, total):
    print("Consoantes encontradas:")
    for consoante in consoantes:
        print(consoante)
    print(f"Total de consoantes: {total}")

caracteres = ler_caracteres()

consoantes, total_consoantes = contar_consoantes(caracteres)

mostrar_consoantes(consoantes, total_consoantes)
