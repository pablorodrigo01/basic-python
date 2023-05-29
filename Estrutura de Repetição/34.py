# 34. Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um
# número inteiro e determine se ele é ou não um número primo.

n = int(input("Digite um número inteiro: "))

# Verifica se o número é maior que 1
if n > 1:
    # Percorre os números de 2 até a raiz quadrada do número
    for i in range(2, int(n**0.5) + 1):
        # Verifica se o número é divisível por algum número dentro desse intervalo
        if n % i == 0:
            print(n, "não é um número primo.")
            break
    else:
        print(n, "é um número primo.")
else:
    print(n, "não é um número primo.")
