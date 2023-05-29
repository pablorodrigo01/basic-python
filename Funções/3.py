# 3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def calcular_soma(a, b, c):
    soma = a + b + c
    return soma

def main():
    # Solicita ao usuário três valores para calcular a soma
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
    c = float(input("Digite o terceiro valor: "))

    # Chama a função calcular_soma passando os valores digitados como argumentos
    resultado = calcular_soma(a, b, c)

    # Exibe o resultado da soma
    print("A soma dos três valores é:", resultado)

# Chama a função principal
main()
