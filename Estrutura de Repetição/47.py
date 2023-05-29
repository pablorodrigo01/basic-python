# 47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o
# nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas

nome_ginasta = input("Nome do ginasta: ")
notas = []

for i in range(7):
    nota = float(input("Nota: "))
    notas.append(nota)

melhor_nota = max(notas)
pior_nota = min(notas)
notas.remove(melhor_nota)
notas.remove(pior_nota)
media = sum(notas) / len(notas)

print("\nResultado final:")
print(f"Atleta: {nome_ginasta}")
print(f"Melhor nota: {melhor_nota}")
print(f"Pior nota: {pior_nota}")
print(f"Média: {media:.2f}")
