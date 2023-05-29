# 8. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contarDigitos(numero):
    if numero == 0:
        return 1

    contador = 0
    numero = abs(numero)  # Garante que consideramos apenas o valor absoluto do número
    
    while numero != 0:
        contador += 1
        numero //= 10

    return contador

# Exemplo de uso da função
numero = int(input("Digite um número inteiro: "))
quantidade_digitos = contarDigitos(numero)
print("A quantidade de dígitos é:", quantidade_digitos)
