# 25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n = int(input("Digite a quantidade de pessoas: "))

soma_idades = 0

for i in range(n):
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
    soma_idades += idade

media_idades = soma_idades / n

if media_idades >= 0 and media_idades <= 25:
    print("A média de idade da turma é de {:.2f}. A turma é considerada jovem.".format(media_idades))
elif media_idades >= 26 and media_idades <= 60:
    print("A média de idade da turma é de {:.2f}. A turma é considerada adulta.".format(media_idades))
else:
    print("A média de idade da turma é de {:.2f}. A turma é considerada idosa.".format(media_idades))
