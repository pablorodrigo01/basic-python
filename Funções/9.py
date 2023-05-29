# 9. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def inverterNumero(numero):
    reverso = 0

    while numero > 0:
        digito = numero % 10
        reverso = (reverso * 10) + digito
        numero //= 10

    return reverso

# Exemplo de uso da função
numero = int(input("Digite um número inteiro: "))
reverso = inverterNumero(numero)
print("O reverso do número é:", reverso)
