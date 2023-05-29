# 4. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def verificar_positivo(numero):
    if numero > 0:
        return 'P' 
    else:
        return 'N' 

def main():
    numero = float(input("Digite um número: "))

    resultado = verificar_positivo(numero)


    print("O resultado é:", resultado)

main()
