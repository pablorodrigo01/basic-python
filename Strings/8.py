# 8. Palíndromo. Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os
# espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

def verificar_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    texto = ''.join(c for c in texto if c.isalnum())

    if texto == texto[::-1]:
        return True
    else:
        return False

sequencia = input("Digite uma sequência de caracteres: ")

if verificar_palindromo(sequencia):
    print("A sequência", sequencia, "é um palíndromo.")
else:
    print("A sequência", sequencia, "não é um palíndromo.")
