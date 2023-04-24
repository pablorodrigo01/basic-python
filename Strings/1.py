# 1.Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo

s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")

print("Conteúdo da primeira string:", s1, "Comprimento:", len(s1))
print("Conteúdo da segunda string:", s2, "Comprimento:", len(s2))

if len(s1) == len(s2):
    if s1 == s2:
        print("As duas strings são iguais")
    else:
        print("As duas strings possuem o mesmo comprimento, mas são diferentes")
else:
    print("As duas strings possuem tamanhos diferentes")
