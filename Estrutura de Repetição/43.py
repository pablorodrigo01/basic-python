# 43. O cardápio de uma lanchonete é o seguinte:
# Especificação Código Preço
# Cachorro Quente 100 R$ 1,20
# Bauru Simples 101 R$ 1,30
# Bauru com ovo 102 R$ 1,50
# Hambúrguer 103 R$ 1,20
# Cheeseburguer 104 R$ 1,30
# Refrigerante 105 R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informarquando o pedido deve ser encerrado

cardapio = {
    100: {"item": "Cachorro Quente", "preco": 1.20},
    101: {"item": "Bauru Simples", "preco": 1.30},
    102: {"item": "Bauru com ovo", "preco": 1.50},
    103: {"item": "Hambúrguer", "preco": 1.20},
    104: {"item": "Cheeseburguer", "preco": 1.30},
    105: {"item": "Refrigerante", "preco": 1.00}
}

total_geral = 0.0

while True:
    codigo = int(input("Digite o código do item (ou 0 para finalizar): "))
    
    if codigo == 0:
        break
    
    if codigo not in cardapio:
        print("Código inválido. Tente novamente.")
        continue
    
    quantidade = int(input("Digite a quantidade desejada: "))
    
    item = cardapio[codigo]
    valor_item = item["preco"] * quantidade
    total_geral += valor_item
    
    print(f"{item['item']}: R$ {valor_item:.2f}")

print(f"\nTotal geral do pedido: R$ {total_geral:.2f}")
