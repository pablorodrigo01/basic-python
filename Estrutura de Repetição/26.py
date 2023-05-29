# 26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato

num_eleitores = int(input("Digite o número total de eleitores: "))

candidato1 = 0
candidato2 = 0
candidato3 = 0

for eleitor in range(1, num_eleitores + 1):
    print("Eleitor", eleitor)
    voto = int(input("Digite o número do candidato (1, 2 ou 3): "))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print("Voto inválido. Eleitor", eleitor, "optou por não votar.")

print("Resultado da eleição:")
print("Candidato 1:", candidato1, "votos")
print("Candidato 2:", candidato2, "votos")
print("Candidato 3:", candidato3, "votos")
