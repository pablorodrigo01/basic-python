# 25. Faça um programa que faça 5 questions para uma pessoa sobre um crime.

question1 = input("Telefonou para a vítima? (sim ou não): ")
question2 = input("Esteve no local do crime? (sim ou não): ")
question3 = input("Mora perto da vítima? (sim ou não): ")
question4 = input("Devia para a vítima? (sim ou não): ")
question5 = input("Já trabalhou com a vítima? (sim ou não): ")

grau = 0
if question1.lower() == "sim":
  grau += 1
if question2.lower() == "sim":
  grau += 1
if question3.lower() == "sim":
  grau += 1
if question4.lower() == "sim":
  grau += 1
if question5.lower() == "sim":
  grau += 1

if grau == 2:
  print("Suspeita")
elif grau >= 3 and grau <= 4:
  print("Cúmplice")
elif grau == 5:
  print("Assassino")
else:
  print("Inocente")