#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre
   # -o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

n1 = float(input("Digite um número: ").replace(",", "."))
n2 = float(input("Digite outro número: ").replace(",", "."))
if n1 > n2:
   maior = n1
   menor = n2
else:
   maior = n2
   menor = n1
soma = n1 + n2
if soma % 2 == 0:
   parImpar = "par"
else:
   parImpar = "ímpar"
multiplicacao = n1 * n2
divisao = maior // menor
print(f"\nA soma dos dois números é: {soma}")
print(f"A multiplicação dos dois números é: {multiplicacao}")
print(f"A divisão inteira dos dois números é: {divisao}")
print(f"O maior dos dois números é: {maior}")
print(f"O número {soma} é {parImpar}")
if multiplicacao > 40:
   div2 = multiplicacao / divisao
   print(f"Como a multiplicação foi maior que 40, o número {multiplicacao} dividido por {divisao} é: {div2}")
else:
   print("A miltiplicação dos números não foi maior que 40!")

