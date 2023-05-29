# 10. Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se
# você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar
# este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def jogar_craps():
    primeiro_lance = lancar_dados()
    print("Você lançou os dados e obteve um total de", primeiro_lance)

    if primeiro_lance == 7 or primeiro_lance == 11:
        print("Natural! Você ganhou!")
        return
    elif primeiro_lance == 2 or primeiro_lance == 3 or primeiro_lance == 12:
        print("Craps! Você perdeu!")
        return

    ponto = primeiro_lance
    print("Seu ponto é", ponto)

    while True:
        lancamento = lancar_dados()
        print("Você lançou os dados e obteve um total de", lancamento)

        if lancamento == ponto:
            print("Você fez o ponto! Você ganhou!")
            return
        elif lancamento == 7:
            print("Você tirou um 7. Você perdeu!")
            return

print("Bem-vindo ao jogo de Craps!")
while True:
    continuar = input("Deseja jogar? (s/n): ")
    if continuar.lower() == "s":
        jogar_craps()
    else:
        break
