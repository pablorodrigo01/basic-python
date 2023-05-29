# 7. Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte: a. quantos espaços em branco existem na frase. b. quantas vezes aparecem as vogais a, e, i, o, u.

def contar_espacos_vogais(frase):
    espacos = frase.count(' ')

    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in frase.lower():
        if letra in vogais:
            vogais[letra] += 1

    print("Quantidade de espaços em branco:", espacos)
    print("Quantidade de vogais:")
    for vogal, quantidade in vogais.items():
        print(f"{vogal}: {quantidade}")

frase = input("Digite uma frase: ")

contar_espacos_vogais(frase)
