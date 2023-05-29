# 37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da
# academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores
# do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

codigo = int(input("Digite o código do cliente (ou 0 para encerrar): "))
altura = float(input("Digite a altura do cliente em metros: "))
peso = float(input("Digite o peso do cliente em kg: "))

mais_alto = mais_baixo = codigo
mais_gordo = mais_magro = codigo
altura_mais_alto = altura_mais_baixo = altura
peso_mais_gordo = peso_mais_magro = peso
soma_alturas = soma_pesos = 0
contador_clientes = 0

while codigo != 0:
    contador_clientes += 1
    soma_alturas += altura
    soma_pesos += peso
    
    if altura > altura_mais_alto:
        mais_alto = codigo
        altura_mais_alto = altura
    
    if altura < altura_mais_baixo:
        mais_baixo = codigo
        altura_mais_baixo = altura
    
    if peso > peso_mais_gordo:
        mais_gordo = codigo
        peso_mais_gordo = peso
    
    if peso < peso_mais_magro:
        mais_magro = codigo
        peso_mais_magro = peso
    
    codigo = int(input("Digite o código do cliente (ou 0 para encerrar): "))
    
    if codigo != 0:
        altura = float(input("Digite a altura do cliente em metros: "))
        peso = float(input("Digite o peso do cliente em kg: "))

if contador_clientes > 0:
    media_alturas = soma_alturas / contador_clientes
    media_pesos = soma_pesos / contador_clientes
else:
    media_alturas = media_pesos = 0

print("\nResultado:")
print("Código do cliente mais alto:", mais_alto)
print("Código do cliente mais baixo:", mais_baixo)
print("Código do cliente mais gordo:", mais_gordo)
print("Código do cliente mais magro:", mais_magro)
print("Média das alturas dos clientes:", media_alturas)
print("Média dos pesos dos clientes:", media_pesos)
