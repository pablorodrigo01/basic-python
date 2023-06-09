# 14. Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar
# um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

def quadrados_magicos():
    ns = list(range(1, 10))

    permutacoes = []
    gerar_permutacoes([], ns, permutacoes)

    for permutacao in permutacoes:
        if verifica_quadrado_magico(permutacao):
            exibir_quadrado_magico(permutacao)


def gerar_permutacoes(atual, ns, permutacoes):
    if len(atual) == 9:
        permutacoes.append(atual.copy())
        return

    for num in ns:
        if num not in atual:
            atual.append(num)
            gerar_permutacoes(atual, ns, permutacoes)
            atual.pop()


def verifica_quadrado_magico(quadrado):
    for i in range(0, 9, 3):
        if sum(quadrado[i:i+3]) != 15:
            return False

    for i in range(3):
        if quadrado[i] + quadrado[i+3] + quadrado[i+6] != 15:
            return False
        
    if quadrado[0] + quadrado[4] + quadrado[8] != 15:
        return False

    if quadrado[2] + quadrado[4] + quadrado[6] != 15:
        return False

    return True


def exibir_quadrado_magico(quadrado):
    for i in range(0, 9, 3):
        print(quadrado[i], quadrado[i+1], quadrado[i+2])
    print()


# Chamada da função para encontrar e exibir os quadrados mágicos
quadrados_magicos()
