# 12. Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode
# retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como
# foram digitados.

import random

def embaralha_palavra(palavra):
    # Converter a palavra para caixa baixa
    palavra = palavra.lower()

    # Embaralhar os caracteres da palavra
    letras = list(palavra)
    random.shuffle(letras)
    palavra_embaralhada = ''.join(letras)

    # Converter a palavra embaralhada para caixa alta
    palavra_embaralhada = palavra_embaralhada.upper()

    return palavra_embaralhada


# Exemplo de uso
palavra = input('Digite uma palavra: ')
palavra_embaralhada = embaralha_palavra(palavra)
print('Palavra embaralhada:', palavra_embaralhada)
