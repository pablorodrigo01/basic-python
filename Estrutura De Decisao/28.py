# 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.

carne = input("Digite o tipo de carne desejado (F - File Duplo, A - Alcatra, P - Picanha): ")
q = float(input("Digite a quantidade desejada (em Kg): "))

if carne == 'F':
    if q <= 5:
        preco = q * 4.9
    else:
        preco = q * 5.8
elif carne == 'A':
    if q <= 5:
        preco = q * 5.9
    else:
        preco = q * 6.8
elif carne == 'P':
    if q <= 5:
        preco = q * 6.9
    else:
        preco = q * 7.8

pagamento = input("Digite o tipo de pagamento (C - Cartão Tabajara, D - Dinheiro): ")

if pagamento == 'C':
    desconto = preco * 0.05
else:
    desconto = 0

print("Tipo de carne: ", carne)
print("Quantidade: ", q, "Kg")
print("Preço total: R$", preco)
print("Tipo de pagamento: ", pagamento)
print("Valor do desconto: R$", desconto)
print("Valor a pagar: R$", preco - desconto)
