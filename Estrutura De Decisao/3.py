# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite o sexo (F/M): ")

sexo = sexo.upper()  # Evitar casos de letras minusculas

if sexo == "F":
    print("Feminino")
elif sexo == "M":
    print("Masculino")
else:
    print("Sexo inválido")
