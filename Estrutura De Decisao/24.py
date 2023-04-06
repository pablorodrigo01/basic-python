# 24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O math da operação deve ser acompanhado de uma frase

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

option = input("Digite a operação desejada (+, -, *, /): ")

if option == "+":
    math = n1 + n2
elif option == "-":
    math = n1 - n2
elif option == "*":
    math = n1 * n2
elif option == "/":
    math = n1 / n2
else:
    print("Operação inválida.")
    math = None

if math is not None:
    print(f"O math da operação é {math}.")
    if math % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
    if math >= 0:
        print("O número é positivo.")
    else:
        print("O número é negativo.")
    if math.is_integer():
        print("O número é inteiro.")
    else:
        print("O número é decimal.")
