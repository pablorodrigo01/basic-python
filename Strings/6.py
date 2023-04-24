# 6. Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

data = input("Digite a sua data de nascimento (dd/mm/aaaa): ")

dia, mes, ano = data.split("/")

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

mes_extenso = meses[int(mes) - 1]

print("Você nasceu em", dia, "de", mes_extenso, "de", ano)
