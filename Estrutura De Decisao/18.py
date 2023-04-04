# 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = map(int, data.split('/'))

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    bissexto = True
else:
    bissexto = False

# Verifica se o mês está dentro do intervalo válido
if mes < 1 or mes > 12:
    print("Data inválida.")
# Verifica se o dia está dentro do intervalo válido para o mês correspondente
elif mes == 2:
    if bissexto:
        if dia < 1 or dia > 29:
            print("Data inválida.")
        else:
            print("Data válida.")
    else:
        if dia < 1 or dia > 28:
            print("Data inválida.")
        else:
            print("Data válida.")
elif mes in [4, 6, 9, 11]:
    if dia < 1 or dia > 30:
        print("Data inválida.")
    else:
        print("Data válida.")
else:
    if dia < 1 or dia > 31:
        print("Data inválida.")
    else:
        print("Data válida.")
