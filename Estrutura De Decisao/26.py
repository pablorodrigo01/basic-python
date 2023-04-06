# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos

l = float(input("Quantos l foram vendidos? "))
tipo = input("Qual é o tipo de combustível? (A-álcool ou G-gasolina) ")
tipo = tipo.upper()

alcool = 1.90
gasolina = 2.50

if tipo == "A":
  if l <= 20:
    valor_total = l * alcool * 0.97
  else:
    valor_total = l * alcool * 0.95
else:
  if l <= 20:
    valor_total = l * gasolina * 0.96
  else:
    valor_total = l * gasolina * 0.94

print(f"O valor total a ser pago é R$ {valor_total:.2f}")
