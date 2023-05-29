# 23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input("Digite um número inteiro: "))

primos = []
divisoes = 0

for num in range(1, n + 1):
    if num < 2:
        continue

    is_primo = True

    for i in range(2, int(num ** 0.5) + 1):
        divisoes += 1
        if num % i == 0:
            is_primo = False
            break

    if is_primo:
        primos.append(num)

print("Números primos entre 1 e", n, ":")
print(primos)
print("Número de divisões executadas:", divisoes)

