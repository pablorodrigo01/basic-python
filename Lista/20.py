# 20. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.

print("Projeção de Gastos com Abono")
print("============================")

salarios = []
abonos = []
valor_minimo = 100
total_gastos = 0
num_minimo = 0

while True:
    salario = float(input("Salário: "))

    if salario == 0:
        break

    abono = salario * 0.2 if salario * 0.2 >= valor_minimo else valor_minimo

    salarios.append(salario)
    abonos.append(abono)
    total_gastos += abono

    if abono == valor_minimo:
        num_minimo += 1

print("\nSalário - Abono")
for i in range(len(salarios)):
    print(f"R$ {salarios[i]:.2f} - R$ {abonos[i]:.2f}")

num_colaboradores = len(salarios)
maior_abono = max(abonos)

print(f"\nForam processados {num_colaboradores} colaboradores")
print(f"Total gasto com abonos: R$ {total_gastos:.2f}")
print(f"Valor mínimo pago a {num_minimo} colaboradores")
print(f"Maior valor de abono pago: R$ {maior_abono:.2f}")
