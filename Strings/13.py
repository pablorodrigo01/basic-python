# 13. Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo
# texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'computador', 'jogo', 'algoritmo']
    
    palavra = random.choice(palavras)
    
    return palavra

def embaralhar_palavra(palavra):
    letras = list(palavra)
    
    # Embaralhar as letras
    random.shuffle(letras)
    
    palavra_embaralhada = ''.join(letras)
    
    return palavra_embaralhada

def jogar_palavra_embaralhada():
    palavra = escolher_palavra()
    palavra_embaralhada = embaralhar_palavra(palavra)
    tentativas = 6
    
    print('Bem-vindo ao jogo da palavra embaralhada!')
    print('Tente adivinhar a palavra correta em até 6 tentativas.')
    print('A palavra embaralhada é:', palavra_embaralhada)
    
    while tentativas > 0:
        palpite = input('Digite o seu palpite: ')
        
        if palpite == palavra:
            print('Parabéns! Você acertou a palavra.')
            return
        
        print('Palpite errado. Tente novamente.')
        tentativas -= 1
        
    print('Você perdeu! A palavra correta era:', palavra)

jogar_palavra_embaralhada()
