# 11. Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.s

def data_por_extenso(data):
    # Dividir a data em dia, mês e ano
    partes = data.split('/')
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])

    # Validação da data
    if not (1 <= dia <= 31) or not (1 <= mes <= 12) or not (1900 <= ano <= 2100):
        return None

    # Dicionário com os meses por extenso
    meses = {
        1: 'janeiro',
        2: 'fevereiro',
        3: 'março',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro'
    }

    # Construir a string de data por extenso
    data_extenso = f'{dia} de {meses[mes]} de {ano}'

    return data_extenso


# Exemplo de uso
data = input('Digite uma data (DD/MM/AAAA): ')
data_extenso = data_por_extenso(data)
if data_extenso is not None:
    print('Data por extenso:', data_extenso)
else:
    print('Data inválida.')
