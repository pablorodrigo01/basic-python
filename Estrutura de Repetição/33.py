# 33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de tempera

temperaturas = []
contador = 0

while True:
    temperatura = float(input("Digite a temperatura (ou 0 para sair): "))
    
    if temperatura == 0:
        break
    
    temperaturas.append(temperatura)
    contador += 1

if contador == 0:
    print("Nenhuma temperatura foi informada.")
else:
    temperatura_minima = min(temperaturas)
    temperatura_maxima = max(temperaturas)
    temperatura_media = sum(temperaturas) / contador
    
    print("Menor temperatura: {:.2f}".format(temperatura_minima))
    print("Maior temperatura: {:.2f}".format(temperatura_maxima))
    print("Média das temperaturas: {:.2f}".format(temperatura_media))
