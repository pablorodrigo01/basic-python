# 45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular
# o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.

gabarito = []
respostas_alunos = []
total_alunos = 0
maior_acerto = 0
menor_acerto = 10
soma_notas = 0

# Obtendo o gabarito da prova
print("Digite as respostas corretas da prova:")
for i in range(1, 11):
    resposta = input(f"Resposta da questão {i}: ")
    gabarito.append(resposta.upper())

while True:
    respostas_aluno = []
    print(f"\nAluno {total_alunos+1}:")
    for i in range(1, 11):
        resposta = input(f"Resposta da questão {i}: ")
        respostas_aluno.append(resposta.upper())

    nota = sum([1 for a, b in zip(respostas_aluno, gabarito) if a == b])

    total_alunos += 1
    soma_notas += nota

    if nota > maior_acerto:
        maior_acerto = nota

    if nota < menor_acerto:
        menor_acerto = nota

    opcao = input("Outro aluno utilizará o sistema? (S/N): ")
    if opcao.upper() != "S":
        break

media = soma_notas / total_alunos

print("\nResultados:")
print(f"Maior acerto: {maior_acerto}")
print(f"Menor acerto: {menor_acerto}")
print(f"Total de alunos que utilizaram o sistema: {total_alunos}")
print(f"Média das notas da turma: {media:.2f}")