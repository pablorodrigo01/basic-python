# 31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser
# informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após
# esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

print("Lojas Tabajara")

while True:
    total_compra = 0.0
    contador_produto = 1

    while True:
        preco_produto = float(input("Produto {}: R$ ".format(contador_produto)))
        if preco_produto == 0:
            break
        total_compra += preco_produto
        contador_produto += 1

    print("Total: R$ {:.2f}".format(total_compra))
    
    dinheiro_cliente = float(input("Dinheiro: R$ "))
    troco = dinheiro_cliente - total_compra
    
    print("Troco: R$ {:.2f}".format(troco))
    
    if troco < 0:
        print("O valor pago é insuficiente. Por favor, refaça o pagamento.")
    else:
        break
