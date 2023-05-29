# 9. Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = 11 - (soma % 11)
    if digito1 >= 10:
        digito1 = 0

    if int(cpf[9]) != digito1:
        return False

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = 11 - (soma % 11)
    if digito2 >= 10:
        digito2 = 0

    if int(cpf[10]) != digito2:
        return False

    return True

cpf = input("Digite o número de CPF no formato xxx.xxx.xxx-xx: ")

if validar_cpf(cpf):
    print("O CPF", cpf, "é válido.")
else:
    print("O CPF", cpf, "é inválido.")
