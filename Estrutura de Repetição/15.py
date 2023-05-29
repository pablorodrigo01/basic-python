# 15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo f

n = int(input("Digite um numero: "))

f1 = 1
f2 = 1

if n == 1:
    print(f1)
elif n == 2:
    print(f1, f2)
else:
    print(f1, f2, end=" ")
    for i in range(3, n + 1):
        nextf = f1 + f2
        print(nextf, end=" ")

        # Atualiza os fs anteriores
        f1 = f2
        f2 = nextf
