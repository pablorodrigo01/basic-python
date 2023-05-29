# 17. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco
# distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta.

while True:
    nome = input("Nome do atleta: ")
    if not nome:
        break

    saltos = []
    for i in range(1, 6):
        distancia = float(input(f"{i}º Salto: "))
        saltos.append(distancia)

    media = sum(saltos) / len(saltos)

    print("Resultado final:")
    print(f"Atleta: {nome}")
    print("Saltos:", " - ".join(map(str, saltos)))
    print(f"Média dos saltos: {media} m")
