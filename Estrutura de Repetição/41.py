# 41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

divida = float(input("Digite o valor da dívida: R$ "))

print("Valor da Dívida\tValor dos Juros\tQuantidade de Parcelas\tValor da Parcela")

# Adiciona os dados da dívida sem juros
print(f"R$ {divida:.2f}\t\t0\t\t\t1\t\t\t\tR$ {divida:.2f}")

# Loop para calcular os dados das demais parcelas com juros
for parcelas, juros in [(3, 0.1), (6, 0.15), (9, 0.2), (12, 0.25)]:
    valor_juros = divida * juros
    valor_total = divida + valor_juros
    valor_parcela = valor_total / parcelas
    print(f"R$ {valor_total:.2f}\t\tR$ {valor_juros:.2f}\t\t{parcelas}\t\t\t\tR$ {valor_parcela:.2f}")
