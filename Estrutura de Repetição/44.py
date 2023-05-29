# 44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são: 1 , 2, 3, 4 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc) 5 - Voto Nulo 6 - Voto em Branco

candidatos = {
    1: "José",
    2: "João",
    3: "Maria",
    4: "Ana"
}

votos = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

total_votos = 0
total_nulos = 0
total_brancos = 0

while True:
    voto = int(input("Digite o código do candidato (ou 0 para encerrar a votação): "))
    
    if voto == 0:
        break
    
    if voto in candidatos:
        votos[voto] += 1
        total_votos += 1
    elif voto == 5:
        total_nulos += 1
        total_votos += 1
    elif voto == 6:
        total_brancos += 1
        total_votos += 1
    else:
        print("Código inválido. Tente novamente.")

print("\nResultado da Eleição")
print("--------------------")

for candidato in candidatos:
    print(f"{candidatos[candidato]}: {votos[candidato]} votos")

print(f"Votos nulos: {total_nulos} votos")
print(f"Votos em branco: {total_brancos} votos")

percentual_nulos = (total_nulos / total_votos) * 100
percentual_brancos = (total_brancos / total_votos) * 100

print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"Percentual de votos em branco: {percentual_brancos:.2f}%")