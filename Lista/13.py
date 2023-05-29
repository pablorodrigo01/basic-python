# 13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperaturas = []

for mes in range(12):
    temperatura = float(input(f"Digite a temperatura média do mês {mes+1}: "))
    temperaturas.append(temperatura)

media_anual = sum(temperaturas) / len(temperaturas)

meses_acima_da_media = []

for mes in range(len(temperaturas)):
    if temperaturas[mes] > media_anual:
        meses_acima_da_media.append(mes + 1)

meses_por_extenso = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

print("Temperaturas acima da média anual:")
for mes in meses_acima_da_media:
    print(f"{mes} - {meses_por_extenso[mes-1]}: {temperaturas[mes-1]}")
