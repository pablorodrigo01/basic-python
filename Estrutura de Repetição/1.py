# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = float(input("Digite uma nota entre zero e dez: "))

    if nota < 0 or nota > 10:
        print("Valor inválido. Digite uma nota entre zero e dez.")
        continue
    else:
        print("Valor válido. A nota é:", nota)
        break
