# 4. Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

nome = input("Digite o seu nome: ")
for i, letra in enumerate(nome):
    print(nome[:i+1])
