# 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências

a = float(input("Digite o valor de A: "))
if a == 0:
    print("A equação não é do segundo grau")
    exit()
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

d = (b*b)-(4*a*c)

if d < 0:
    print("A equação não possui raizes reais")
    exit()
elif d == 0:
    r1 = (-b + float(d) ** 0.5)/(2*a)
    print("A equação possui apenas uma raiz real:", r1)
else:
    r1 = (-b + float(d) ** 0.5)/(2*a)
    r2 = (-b - float(d) ** 0.5)/(2*a)
    print(f'A equação possui duas raizes real: {r1} e {r2}')
