# 10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores

A = []
B = []

print("Digite os elementos do vetor A:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    A.append(elemento)

print("Digite os elementos do vetor B:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    B.append(elemento)

C = []
for i in range(10):
    C.append(A[i])
    C.append(B[i])

print("Vetor C (valores intercalados de A e B):")
print(C)
