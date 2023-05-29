# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita config a operação

config = True

while config:
    try:
        populacao_a = int(input("Digite o número de população A: "))
        populacao_b = int(input("Digite o número de população B: "))
        taxa_crescimento_a = float(input("Digite a taxa de crescimento da população A (%): "))
        taxa_crescimento_b = float(input("Digite a taxa de crescimento da população B (%): "))

        anos = 0

        while populacao_a < populacao_b:
            anos += 1
            populacao_a *= (1 + taxa_crescimento_a / 100)
            populacao_b *= (1 + taxa_crescimento_b / 100)

        print("Serão necessários", anos, "anos para que a população do país A ultrapasse ou iguale a população do país B.")

        opcao = input("Deseja continuar a operação? (S/N): ")
        if opcao.upper() != 'S':
            config = False
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros para as populações e números decimais para as taxas de crescimento.")