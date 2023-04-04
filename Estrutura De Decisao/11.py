# 11. As Organizações Tabajara resolveram dar um up de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes

sal = float(input("Digite o salário do colaborador: "))

if sal <= 280:
    percentual = 20
elif sal <= 700:
    percentual = 15
elif sal <= 1500:
    percentual = 10
else:
    percentual = 5
up = sal * percentual / 100
novo_sal = sal + up

print(f"Salário antes do reajuste: R$ {sal:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {up:.2f}")
print(f"Novo salário após o aumento: R$ {novo_sal:.2f}")
