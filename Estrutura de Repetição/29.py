# 29. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que
# o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços.

print("Lojas Quase Dois - Tabela de preços")

for quantidade in range(1, 51):
    preco = quantidade * 1.99
    print(quantidade, "- R$ {:.2f}".format(preco))
