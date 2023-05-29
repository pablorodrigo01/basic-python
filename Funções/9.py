# 9. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def invertern(n):
    reverso = 0

    while n > 0:
        digito = n % 10
        reverso = (reverso * 10) + digito
        n //= 10

    return reverso

n = int(input("Digite um número inteiro: "))
reverso = invertern(n)
print("O reverso do número é:", reverso)
