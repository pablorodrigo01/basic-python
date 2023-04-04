# 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

num = int(input("Digite um número inteiro menor que 1000: "))

if num >= 1000:
    print("O número deve ser menor que 1000.")
else:
    centenas = num // 100
    dezenas = (num % 100) // 10
    unidades = num % 10

    texto_centenas = "centena" if centenas == 1 else "centenas"
    texto_dezenas = "dezena" if dezenas == 1 else "dezenas"
    texto_unidades = "unidade" if unidades == 1 else "unidades"

    texto = ""
    if centenas > 0:
        texto += f"{centenas} {texto_centenas}"
        if dezenas > 0 and unidades > 0:
            texto += ", "
        elif dezenas > 0 or unidades > 0:
            texto += " e "
    if dezenas > 0:
        texto += f"{dezenas} {texto_dezenas}"
        if unidades > 0:
            texto += " e "
    if unidades > 0 or num == 0:
        texto += f"{unidades} {texto_unidades}"

    print(f"O número {num} tem {texto}.")
