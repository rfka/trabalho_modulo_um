#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um 
#   - crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

nao = sim = 0
resposta = []
print("=" *80)
print("Programa Investigativo")
print("=" *80)
print("Questionário!!! Responda somente com [S] ou [N] !!!")
print("Por acaso voce...")
resposta.append(str(input("\n...telefonou para a vítima? ")))
resposta.append(str(input("...esteve no local do crime? ")))
resposta.append(str(input("...mora perto da vítima? ")))
resposta.append(str(input("...devia para a vítima? ")))
resposta.append(str(input("...já trabalhou com a vítima? \n")))
print("=" * 30)

aux = resposta.count("s")

if aux == 5:
    print("===      Assassino!!!      ===")
elif aux == 3 or aux == 4:
    print("===      Cúmplice!!!       ===")
elif aux == 2:
    print("===   Voce é suspeito!!!   ===")
else:
    print("===   Voce é Inocente!!!   ===")
print("=" * 30)
print()
