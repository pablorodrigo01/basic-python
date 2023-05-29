# 40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# a. Código da cidade;
# b. Número de veículos de passeio (em 1999);
# c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e. Qual a média de veículos nas cinco cidades juntas;
# f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

maior_indice_acidentes = 0
menor_indice_acidentes = float('inf')
cidade_maior_indice = ''
cidade_menor_indice = ''
soma_veiculos = 0
soma_acidentes_menos_2000 = 0
contador_cidades_menos_2000 = 0

for i in range(1, 6):
    codigo_cidade = int(input(f"Digite o código da cidade {i}: "))
    veiculos_passeio = int(input("Digite o número de veículos de passeio (em 1999): "))
    acidentes_transito = int(input("Digite o número de acidentes de trânsito com vítimas (em 1999): "))

    if acidentes_transito > maior_indice_acidentes:
        maior_indice_acidentes = acidentes_transito
        cidade_maior_indice = codigo_cidade

    if acidentes_transito < menor_indice_acidentes:
        menor_indice_acidentes = acidentes_transito
        cidade_menor_indice = codigo_cidade

    soma_veiculos += veiculos_passeio

    if veiculos_passeio < 2000:
        soma_acidentes_menos_2000 += acidentes_transito
        contador_cidades_menos_2000 += 1

media_veiculos = soma_veiculos / 5
media_acidentes_menos_2000 = soma_acidentes_menos_2000 / contador_cidades_menos_2000

print("\nEstatísticas das cidades:")
print("Maior índice de acidentes de trânsito:", maior_indice_acidentes, "- Cidade:", cidade_maior_indice)
print("Menor índice de acidentes de trânsito:", menor_indice_acidentes, "- Cidade:", cidade_menor_indice)
print("Média de veículos nas cinco cidades juntas:", media_veiculos)
print("Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio:", media_acidentes_menos_2000)
