# 21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

valor_saque = int(input("Digite o valor do saque (entre R$10 e R$600): "))

if valor_saque < 10 or valor_saque > 600:
    print("Valor inválido. Tente novamente.")
else:
    notas_100 = valor_saque // 100
    valor_saque %= 100

    notas_50 = valor_saque // 50
    valor_saque %= 50

    notas_10 = valor_saque // 10
    valor_saque %= 10

    notas_5 = valor_saque // 5
    valor_saque %= 5

    notas_1 = valor_saque

    print(f"Notas de R$100: {notas_100}")
    print(f"Notas de R$50: {notas_50}")
    print(f"Notas de R$10: {notas_10}")
    print(f"Notas de R$5: {notas_5}")
    print(f"Notas de R$1: {notas_1}")
