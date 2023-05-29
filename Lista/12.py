# 12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []

for i in range(30):
    idade = int(input(f"Digite a idade do {i+1}º aluno: "))
    altura = float(input(f"Digite a altura do {i+1}º aluno: "))
    idades.append(idade)
    alturas.append(altura)

media_alturas = sum(alturas) / len(alturas)

contador = 0
for i in range(len(idades)):
    if idades[i] > 13 and alturas[i] < media_alturas:
        contador += 1

print(f"Número de alunos com mais de 13 anos e altura inferior à média: {contador}")
