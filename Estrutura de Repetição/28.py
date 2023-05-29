# 28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade_cds = int(input("Digite a quantidade de CDs na coleção: "))
total_investido = 0

for cd in range(1, quantidade_cds + 1):
    valor_cd = float(input("Digite o valor gasto no CD {}: ".format(cd)))
    total_investido += valor_cd

media_gasto = total_investido / quantidade_cds

print("O valor total investido na coleção de CDs é:", total_investido)
print("O valor médio gasto em cada CD é:", media_gasto)
