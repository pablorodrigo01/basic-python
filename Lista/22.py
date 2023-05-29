# 22. Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles

mouses = {
    1: "necessita da esfera",
    2: "necessita de limpeza",
    3: "necessita troca do cabo ou conector",
    4: "quebrado ou inutilizado"
}

quantidade_mouses = 0
situacoes = {
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

while True:
    identificacao = int(input("Número de identificação do mouse (0 para encerrar): "))
    if identificacao == 0:
        break
    
    defeito = int(input("Tipo de defeito (1 - necessita da esfera, 2 - necessita de limpeza, 3 - necessita troca do cabo ou conector, 4 - quebrado ou inutilizado): "))
    if defeito not in mouses:
        print("Defeito inválido. Tente novamente.")
        continue
    
    quantidade_mouses += 1
    situacoes[defeito] += 1

print("\nRelatório:")
print(f"Quantidade de mouses: {quantidade_mouses}")
print("Situação\tQuantidade\tPercentual")
for defeito, quantidade in situacoes.items():
    percentual = quantidade / quantidade_mouses * 100
    print(f"{defeito}- {mouses[defeito]}\t{quantidade}\t{percentual:.2f}%")
