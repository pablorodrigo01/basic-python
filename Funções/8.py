# 8. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contarDigitos(n):
    if n == 0:
        return 1

    contador = 0
    n = abs(n)
    
    while n != 0:
        contador += 1
        n //= 10

    return contador

n = int(input("Digite um número inteiro: "))
quantidade_digitos = contarDigitos(n)
print("A quantidade de dígitos é:", quantidade_digitos)
