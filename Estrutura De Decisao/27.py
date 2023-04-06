# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços

morango_p = float(input("Quantos Kg de morangos foram comprados? "))
maca_p = float(input("Quantos Kg de maçãs foram compradas? "))

morango_v = 2.50 if morango_p <= 5 else 2.20
maca_v = 1.80 if maca_p <= 5 else 1.50

valor_bruto = morango_p * morango_v + maca_p * maca_v

if morango_p + maca_p > 8 or valor_bruto > 25:
  valor_off = valor_bruto * 0.9
else:
  valor_off = valor_bruto

print(f"O valor total da compra é R$ {valor_off:.2f}")
