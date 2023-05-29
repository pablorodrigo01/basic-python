# 35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

limite = int(input("Digite um número inteiro: "))

primos = []

for n in range(2, limite + 1):
    eh_primo = True
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            eh_primo = False
            break
    if eh_primo:
        primos.append(n)

print("Números primos até", limite, ":")
print(primos)
