# 19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000

n1 = int(input("Digite a quantia de numeros: "))

ns = []
for i in range(n1):
    c = float(input("Digite um numero: "))

    while c < 0 or c > 1000:
        print("Erro")
        c = float(input("Digite um numero: "))

    ns.append(c)

menor = min(ns)
maior = max(ns)
soma = sum(ns)

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Soma dos valores:", soma)