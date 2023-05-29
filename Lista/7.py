# 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números

def calcular_soma(vetor):
    return sum(vetor)

def calcular_multiplicacao(vetor):
    resultado = 1
    for num in vetor:
        resultado *= num
    return resultado

vetor = []
for i in range(5):
    num = int(input(f"Digite o número {i+1}: "))
    vetor.append(num)

soma = calcular_soma(vetor)

multiplicacao = calcular_multiplicacao(vetor)

print("Números:", vetor)
print("Soma:", soma)
print("Multiplicação:", multiplicacao)
