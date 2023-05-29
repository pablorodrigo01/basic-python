# 18. Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas
# telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
# correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número

def calcular_percentual(votos, total_votos):
    return (votos / total_votos) * 100

num_jogadores = 23
votos = [0] * num_jogadores
total_votos = 0

print("Enquete: Quem foi o melhor jogador?")

while True:
    jogador = int(input("Número do jogador (0=fim): "))

    if jogador == 0:
        break

    if jogador < 1 or jogador > num_jogadores:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
        continue

    votos[jogador - 1] += 1
    total_votos += 1

print("Resultado da votação:")
print(f"Foram computados {total_votos} votos.")

with open("resultado_enquete.txt", "w") as arquivo:
    for i, num_votos in enumerate(votos):
        if num_votos > 0:
            percentual = calcular_percentual(num_votos, total_votos)
            print(f"Jogador {i + 1}: {num_votos} voto(s) {percentual:.1f}%")

            arquivo.write(f"Jogador {i + 1}: {num_votos} voto(s) {percentual:.1f}%\n")

    melhor_jogador = votos.index(max(votos)) + 1
    maior_votos = max(votos)
    percentual_melhor_jogador = calcular_percentual(maior_votos, total_votos)

    print(f"O melhor jogador foi o número {melhor_jogador}, com {maior_votos} voto(s), correspondendo a {percentual_melhor_jogador:.1f}% do total de votos.")

    arquivo.write(f"O melhor jogador foi o número {melhor_jogador}, com {maior_votos} voto(s), correspondendo a {percentual_melhor_jogador:.1f}% do total de votos.\n")
    