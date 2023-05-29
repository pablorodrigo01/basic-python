# 11. Altere o programa anterior para mostrar no final a soma dos números

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

soma = 0

if n1 <= n2:
    for n in range(n1, n2 + 1):
        print(n)
        soma += n
else:
    for n in range(n1, n2 - 1, -1):
        print(n)
        soma += n

print("Soma:", soma)
