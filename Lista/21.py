# 21. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível.

carros = []
consumo = []
preco_gasolina = 2.25

for i in range(5):
    print(f"Veículo {i+1}")
    modelo = input("Nome: ")
    km_por_litro = float(input("Km por litro: "))
    
    carros.append(modelo)
    consumo.append(km_por_litro)

menor_consumo = min(consumo)
indice_menor_consumo = consumo.index(menor_consumo)
modelo_menor_consumo = carros[indice_menor_consumo]

print("\nRelatório Final")
for i in range(5):
    litros_consumidos = 1000 / consumo[i]
    valor_gasto = litros_consumidos * preco_gasolina
    print(f"{i+1} - {carros[i]} - {consumo[i]} - {litros_consumidos:.1f} litros - R$ {valor_gasto:.2f}")

print(f"\nO menor consumo é do {modelo_menor_consumo}.")
