# 23. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos
# usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt

def converter_bytes_para_megabytes(bytes):
    megabytes = bytes / (1024 * 1024)
    return megabytes


def calcular_percentual_uso(espaco, espaco_total):
    percentual = (espaco / espaco_total) * 100
    return percentual

usuarios = []
espaco_total = 0

with open("usuarios.txt", "r") as arquivo:
    for linha in arquivo:
        usuario, espaco = linha.split()
        espaco = int(espaco)
        usuarios.append((usuario, espaco))
        espaco_total += espaco

usuarios.sort(key=lambda x: x[1], reverse=True)

espaco_medio = espaco_total / len(usuarios)

# Geração do relatório "relatorio.txt"
with open("relatorio.txt", "w") as relatorio:
    relatorio.write("ACME Inc. Uso do espaço em disco pelos usuários\n")
    relatorio.write("-" * 80 + "\n")
    relatorio.write("{:<4s} {:<15s} {:<15s} {:<10s}\n".format("Nr.", "Usuário", "Espaço utilizado", "% do uso"))

    for i, (usuario, espaco) in enumerate(usuarios, start=1):
        espaco_mb = converter_bytes_para_megabytes(espaco)
        percentual_uso = calcular_percentual_uso(espaco, espaco_total)
        relatorio.write("{:<4d} {:<15s} {:.2f} MB {:<7.2f}%\n".format(i, usuario, espaco_mb, percentual_uso))

    relatorio.write("\nEspaço total ocupado: {:.2f} MB\n".format(converter_bytes_para_megabytes(espaco_total)))
    relatorio.write("Espaço médio ocupado: {:.2f} MB\n".format(converter_bytes_para_megabytes(espaco_medio)))

print("Relatório gerado com sucesso.")
