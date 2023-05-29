# 14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

for pergunta in perguntas:
    resposta = input(pergunta + " (Sim ou Não): ")
    if resposta.lower() == "sim":
        respostas.append(True)
    else:
        respostas.append(False)

contador = respostas.count(True)

if contador == 2:
    classificacao = "Suspeita"
elif 3 <= contador <= 4:
    classificacao = "Cúmplice"
elif contador == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print("Classificação: ", classificacao)
