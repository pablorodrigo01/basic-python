# 3. Faça um programa que leia e valide as seguintes informações: a. Nome: maior que 3 caracteres; b. Idade: entre 0 e 150; c. Salário: maior que zero d. Sexo: 'f' ou 'm'; e. Estado Civil: 's', 'c', 'v', 'd';
while True:
    nome = input("Digite o seu nome (maior que 3 caracteres): ")
    if len(nome) <= 3:
        print("Erro: o nome deve ter mais de 3 caracteres. Tente novamente.")
        continue

    idade = int(input("Digite a sua idade (entre 0 e 150): "))
    if idade < 0 or idade > 150:
        print("Erro: a idade deve estar entre 0 e 150. Tente novamente.")
        continue

    salario = float(input("Digite o seu salário (maior que zero): "))
    if salario <= 0:
        print("Erro: o salário deve ser maior que zero. Tente novamente.")
        continue

    sexo = input("Digite o seu sexo (f/m): ")
    sexo = sexo.lower()
    if sexo not in ['f', 'm']:
        print("Erro: o sexo deve ser 'f' ou 'm'. Tente novamente.")
        continue

    estado_civil = input("Digite o seu estado civil (s/c/v/d): ")
    estado_civil = estado_civil.lower()
    if estado_civil not in ['s', 'c', 'v', 'd']:
        print("Erro: o estado civil deve ser 's', 'c', 'v' ou 'd'. Tente novamente.")
        continue

    print("Informações validadas com sucesso.")
    break
