# 16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um
# total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários

contadores = [0] * 10

while True:
    salario = float(input("Informe o salário do vendedor (ou -1 para encerrar): "))
    if salario == -1:
        break
    
    salario_total = 200 + salario * 0.09
    
    posicao = int(salario_total / 100)
    if posicao > 9:
        posicao = 9
    
    contadores[posicao] += 1

faixas = ["$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599", "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999", "$1000 em diante"]
for i in range(10):
    print(f"Quantidade de vendedores na faixa salarial {faixas[i]}: {contadores[i]}")
