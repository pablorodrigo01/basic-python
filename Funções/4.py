# 4. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def verificar_positivo(numero):
    if numero > 0:
        return 'P'  # Retorna 'P' se o número for positivo
    else:
        return 'N'  # Retorna 'N' se o número for zero ou negativo

def main():
    # Solicita ao usuário um número para verificar se é positivo
    numero = float(input("Digite um número: "))

    # Chama a função verificar_positivo passando o número digitado como argumento
    resultado = verificar_positivo(numero)

    # Exibe o resultado
    print("O resultado é:", resultado)

# Chama a função principal
main()
