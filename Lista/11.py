# 11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

A = []
B = []
C = []

print("Digite os elementos do vetor A:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    A.append(elemento)

print("Digite os elementos do vetor B:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    B.append(elemento)

print("Digite os elementos do vetor C:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    C.append(elemento)

D = []
for i in range(10):
    D.append(A[i])
    D.append(B[i])
    D.append(C[i])

print("Vetor D (valores intercalados de A, B e C):")
print(D)
