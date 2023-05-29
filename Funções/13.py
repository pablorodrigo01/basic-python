# 13. Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor
# mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

def desenha_moldura(linhas=1, colunas=1):
    # Limitar os valores de linhas e colunas dentro da faixa de 1 a 20
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    # Desenhar a moldura
    print('+' + '-' * (colunas - 2) + '+')
    for _ in range(linhas - 2):
        print('|' + ' ' * (colunas - 2) + '|')
    print('+' + '-' * (colunas - 2) + '+')


# Exemplo de uso
linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))
desenha_moldura(linhas, colunas)
