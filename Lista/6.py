# 6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

def calcular_media(notas):
    return sum(notas) / len(notas)

def ler_notas_alunos():
    notas_alunos = []
    for i in range(10):
        notas = []
        for j in range(4):
            nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
            notas.append(nota)
        notas_alunos.append(notas)
    return notas_alunos

def contar_alunos_aprovados(media_alunos):
    count = 0
    for media in media_alunos:
        if media >= 7.0:
            count += 1
    return count

# Ler as notas dos alunos
notas_alunos = ler_notas_alunos()

# Calcular a média de cada aluno
medias = []
for notas in notas_alunos:
    media = calcular_media(notas)
    medias.append(media)

# Contar o número de alunos com média maior ou igual a 7.0
aprovados = contar_alunos_aprovados(medias)

# Imprimir o resultado
print(f"Número de alunos com média maior ou igual a 7.0: {aprovados}")
