# 15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).

notas = []

while True:
    nota = float(input("Informe a nota (-1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

quantidade = len(notas)
print("Quantidade de valores lidos:", quantidade)

print("Valores informados:", end=" ")
for nota in notas:
    print(nota, end=" ")
print()

print("Valores na ordem inversa:")
for nota in reversed(notas):
    print(nota)

soma = sum(notas)
print("Soma dos valores:", soma)

media = soma / quantidade
print("Média dos valores:", media)

acima_media = len([nota for nota in notas if nota > media])
print("Quantidade de valores acima da média:", acima_media)

abaixo_sete = len([nota for nota in notas if nota < 7])
print("Quantidade de valores abaixo de sete:", abaixo_sete)

print("Programa encerrado.")
