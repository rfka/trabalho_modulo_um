#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA 
#   - e devolva uma string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e 
#   - retorne 'data inválida' caso a data seja inválida.

def mesExtenso(mes):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    print("O mes por extenso que vc digitou é: %s"%(meses[mes]))

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia,mes,ano = data.split("/")
ano = int(ano)
if mes == "02" and dia > "28":
    if (ano%4 == 0 and ano%100 != 0) or ano%400 == 0:
        mes = int(mes)-1
        mesExtenso(mes)
    else: 
        print("Voce digitou uma data inválida!")
elif mes in "01,03,05,07,08,10,12" and dia > "31":
    print("Voce digitou uma data inválida!")
elif mes in "04,06,09,11" and dia >"30":
    print("Voce digitou uma data inválida!")
else:
    mes = int(mes)-1
    mesExtenso(mes)