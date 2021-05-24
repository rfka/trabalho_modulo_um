#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que 
#  -receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece 
#  -as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma 
#  -vogal.
aux = 0

frase = str(input("Digite uma frase: ").lower())

for cont in frase:
    if cont in "aeiou":
        aux +=1

for i in "aeiouàáâãéêíóõôú":
    frase = frase.replace(i, " ")

print(f"A quantidade de vogais contida na frase é: {aux}")
print(f"A frase sem as vogais ficou assim: {frase}")