# 16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

f1 = 0
f2 = 1

print(f1, f2, end=" ")

while f2 <= 500:
    nextf = f1 + f2

    if nextf > 500:
        break

    print(nextf, end=" ")

    f1 = f2
    f2 = nextf

print()
