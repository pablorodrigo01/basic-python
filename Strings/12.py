# 12. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador

def corrigir_numero_telefone(telefone):
    telefone = telefone.replace('-', '').replace(' ', '')
    
    if len(telefone) == 7:
        telefone_corrigido = '3' + telefone
        telefone_formatado = telefone_corrigido[:4] + '-' + telefone_corrigido[4:]
        
        print('Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.')
        print('Telefone corrigido sem formatação:', telefone_corrigido)
        print('Telefone corrigido com formatação:', telefone_formatado)
    else:
        print('Telefone válido:', telefone)

telefone = input('Telefone: ')
corrigir_numero_telefone(telefone)
