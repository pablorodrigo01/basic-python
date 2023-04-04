# 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o sind e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

valor = float(input("Digite o valor da hora trabalhada: "))
hora = int(input("Digite a quantiadade de horas trabalhada: "))

sal_bruto = valor * hora
fgts = sal_bruto * 0.11
sind = sal_bruto * 0.03

if sal_bruto <= 900:
    ir = 0
elif sal_bruto <= 1500:
    ir = 5
elif sal_bruto <= 2500:
    ir = 10
else:
    ir = 20

sal_liquido = sal_bruto - ir - sind

print(f"Salário Bruto: R$ {sal_bruto:.2f}")
print(f"(-) IR ({ir*100/sal_bruto:.0f}%): R$ {ir:.2f}")
print(f"(-) sind ({sind*100/sal_bruto:.0f}%): R$ {sind:.2f}")
print(f"FGTS ({fgts*100/sal_bruto:.0f}%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {ir+sind:.2f}")
print(f"Salário Líquido: R$ {sal_liquido:.2f}")
