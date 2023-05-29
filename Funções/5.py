# 5. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    imposto = custo * taxaImposto / 100
    custo += imposto
    return custo

def main():
    taxa = float(input("Digite a taxa de imposto (%): "))
    valor = float(input("Digite o custo do item: "))

    custo_com_imposto = somaImposto(taxa, valor)

    print("Custo com imposto: R$", custo_com_imposto)

main()
