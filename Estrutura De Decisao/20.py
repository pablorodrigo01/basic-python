# 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print(f"Média: {media:.1f}. Aprovado com Distinção.")
elif media >= 7:
    print(f"Média: {media:.1f}. Aprovado.")
else:
    print(f"Média: {media:.1f}. Reprovado.")
