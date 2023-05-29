# 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

def separar_par_impar(ns):
    par = []
    impar = []
    for num in ns:
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    return par, impar

def ler_ns():
    ns = []
    for i in range(20):
        num = int(input(f"Digite o número {i+1}: "))
        ns.append(num)
    return ns

def imprimir_vetores(ns, par, impar):
    print("Números digitados:")
    print(ns)
    print("Números pares:")
    print(par)
    print("Números ímpares:")
    print(impar)

ns = ler_ns()

par, impar = separar_par_impar(ns)

imprimir_vetores(ns, par, impar)
