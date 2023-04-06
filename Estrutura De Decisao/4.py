# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

letra = letra.upper()

if letra.isalpha():  # Uso do isalpha pra evitar a entrada de numeros
    if letra in 'AEIOU':
        print("A letra digitada é uma vogal.")
    else:
        print("A letra digitada é uma consoante.")
else:
    print("A entrada digitada não é uma letra.")
