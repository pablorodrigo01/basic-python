# 1. Faça um programa que peça uma n, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    n = float(input("Digite uma n entre zero e dez: "))

    if n < 0 or n > 10:
        print("Valor inválido. Digite uma n entre zero e dez.")
        continue
    else:
        print("Valor válido. A n é:", n)
        break
