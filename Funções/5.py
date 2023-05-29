# 5. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    imposto = custo * taxaImposto / 100  # Calcula o valor do imposto com base na taxa
    custo += imposto  # Adiciona o imposto ao custo
    return custo

def main():
    # Solicita ao usuário a taxa de imposto e o custo do item
    taxa = float(input("Digite a taxa de imposto (%): "))
    valor = float(input("Digite o custo do item: "))

    # Chama a função somaImposto passando a taxa de imposto e o custo do item como argumentos
    custo_com_imposto = somaImposto(taxa, valor)

    # Exibe o resultado
    print("Custo com imposto: R$", custo_com_imposto)

# Chama a função principal
main()
