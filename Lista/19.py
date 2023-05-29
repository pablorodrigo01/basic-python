# 19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações

opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = [0] * len(opcoes)
total_votos = 0

print("Enquete: Qual o melhor Sistema Operacional para uso em servidores?")
print("Digite o número correspondente à opção desejada:")
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- Mac OS")
print("6- Outro")

while True:
    voto = int(input("Voto (0 para encerrar): "))

    if voto == 0:
        break

    if voto < 1 or voto > len(opcoes):
        print("Opção inválida. Tente novamente.")
        continue

    votos[voto - 1] += 1
    total_votos += 1

print("Sistema Operacional   Votos   %")
print("-------------------   -----   ---")

for i in range(len(opcoes)):
    percentual = (votos[i] / total_votos) * 100
    print(f"{opcoes[i]:20}   {votos[i]:<6}   {percentual:>3.0f}%")

print("-------------------   -----   -----")
print(f"Total                 {total_votos}")

indice_vencedor = votos.index(max(votos))
vencedor = opcoes[indice_vencedor]
votos_vencedor = votos[indice_vencedor]
percentual_vencedor = (votos_vencedor / total_votos) * 100

print(f"\nO Sistema Operacional mais votado foi o {vencedor}, com {votos_vencedor} voto(s), correspondendo a {percentual_vencedor:.0f}% dos votos.")
