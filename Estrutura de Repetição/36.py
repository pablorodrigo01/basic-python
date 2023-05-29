# 36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário

numero = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

if fim < inicio:
    print("Erro: o valor final não pode ser menor que o valor inicial.")
else:
    print("Vou montar a tabuada de", numero, "começando em", inicio, "e terminando em", fim, ":")

    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(numero, "X", i, "=", resultado)
