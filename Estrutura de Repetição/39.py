# 39. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

aluno_mais_alto = 0
altura_mais_alto = 0
aluno_mais_baixo = 0
altura_mais_baixo = 0

for i in range(1, 11):
    aluno = int(input("Digite o número do aluno: "))
    altura = float(input("Digite a altura do aluno em centímetros: "))
    
    if i == 1:
        aluno_mais_alto = aluno
        altura_mais_alto = altura
        aluno_mais_baixo = aluno
        altura_mais_baixo = altura
    else:
        if altura > altura_mais_alto:
            aluno_mais_alto = aluno
            altura_mais_alto = altura
        if altura < altura_mais_baixo:
            aluno_mais_baixo = aluno
            altura_mais_baixo = altura

print("\nAluno mais alto:")
print("Número do aluno:", aluno_mais_alto)
print("Altura:", altura_mais_alto, "cm")

print("\nAluno mais baixo:")
print("Número do aluno:", aluno_mais_baixo)
print("Altura:", altura_mais_baixo, "cm")
