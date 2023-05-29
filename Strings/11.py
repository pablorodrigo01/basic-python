# 11. Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

import random

palavras = ['ABACAXI', 'BANANA', 'CENOURA', 'DAMASCO', 'ESPINAFRE', 'FIGO', 'GOIABA', 'HORTELA']

def escolher_palavra():
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    palavra_secreta = ['_'] * len(palavra)
    erros = 0
    letras_erradas = []

    print('Jogo da Forca')

    while True:
        letra = input('Digite uma letra: ').upper()

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_secreta[i] = letra

            print('A palavra é:', ' '.join(palavra_secreta))

            if '_' not in palavra_secreta:
                print('Parabéns! Você acertou a palavra!')
                break
        else:
            erros += 1
            letras_erradas.append(letra)
            print(f'-> Você errou pela {erros}ª vez. Tente de novo!')

            if erros == 6:
                print(f'Você foi enforcado! A palavra era: {palavra}')
                break

        print('Letras erradas:', ' '.join(letras_erradas))

jogar_forca()
