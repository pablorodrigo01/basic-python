# 10. Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

def numero_por_extenso(numero):
    numeros_ate_19 = [
        "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
        "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"
    ]

    dezenas = [
        "", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"
    ]

    if numero < 0 or numero > 99:
        return "Número inválido. Digite um número entre 0 e 99."

    if numero <= 19:
        return numeros_ate_19[numero]

    dezena = numero // 10
    unidade = numero % 10
    if unidade == 0:
        return dezenas[dezena]
    else:
        return dezenas[dezena] + " e " + numeros_ate_19[unidade]

numero = int(input("Digite um número até 99: "))

extenso = numero_por_extenso(numero)
print(extenso)
