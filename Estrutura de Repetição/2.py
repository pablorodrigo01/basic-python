# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    nome = input("Digite o seu nome de usuário: ")
    senha = input("Digite a sua senha: ")
    
    if senha == nome:
        print("Erro: a senha não pode ser igual ao nome de usuário. Tente novamente.")
        continue
    else:
        print("Usuário e senha registrados com sucesso.")
        break
