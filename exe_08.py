#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
#   - (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário 
#   - receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade,
#   - com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir
#   - por 35 anos para se aposentar.

import datetime
dataAtual = datetime.datetime.now()
anoAtual = dataAtual.year
cadastro = dict()

cadastro["nome"] = str(input("Digite o nome do funcionário: "))
cadastro["dataNascimento"] = int(input("Digite o ano de nascimento do funcionário: "))
cadastro["ctps"] = int(input("Digite o numero da CTPS para o funcionário. Se não tiver, digite 0: "))
if cadastro["ctps"] != 0:
    cadastro["anoContratacao"] = int(input("Digite o ano de contratação do funcionário: "))
    cadastro["salario"] = float(input("Digite o salário do funcionário: "))
    cadastro["idade"] = (anoAtual - cadastro["dataNascimento"])
    cadastro["aposentadoria"] = (35 - (anoAtual - cadastro["anoContratacao"]))+ cadastro["idade"]
else:
    print("Sem registro na CTPS!")

for k, v in cadastro.items():
    print(f"{k} é {v} !")

