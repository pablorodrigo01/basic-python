# 6. Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos
# duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para
# registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def converterHora(horas, minutos):
    if horas > 12:
        horas -= 12
        periodo = 'P.M.'
    else:
        periodo = 'A.M.'
    
    return horas, minutos, periodo

def imprimirHora(horas, minutos, periodo):
    print(f"{horas}:{minutos:02d} {periodo}")

def main():
    while True:
        # Solicita ao usuário a hora e os minutos
        horas = int(input("Digite a hora (0-23): "))
        minutos = int(input("Digite os minutos (0-59): "))

        # Chama a função converterHora passando as horas e os minutos como argumentos
        nova_hora, novos_minutos, periodo = converterHora(horas, minutos)

        # Chama a função imprimirHora para exibir a hora convertida
        imprimirHora(nova_hora, novos_minutos, periodo)

        # Pergunta ao usuário se deseja converter uma nova hora
        opcao = input("Deseja converter outra hora? (S/N): ")
        if opcao.upper() != 'S':
            break

# Chama a função principal
main()
