# 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media == 10:
    print(f"Média: {media:.1f}. Aprovado com Distinção.")
elif media >= 7:
    print(f"Média: {media:.1f}. Aprovado.")
else:
    print(f"Média: {media:.1f}. Reprovado.")
