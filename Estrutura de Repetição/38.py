# 38. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Ap

ano_atual = int(input("Digite o ano atual: "))

salario_inicial = 1000.0
percentual_aumento = 0.015  # 1,5% em decimal

for ano in range(1996, ano_atual + 1):
    aumento = percentual_aumento * salario_inicial
    salario_inicial += aumento
    percentual_aumento *= 2

salario_atual = round(salario_inicial, 2)

print("O salário atual do funcionário em", ano_atual, "é de R$", salario_atual)
