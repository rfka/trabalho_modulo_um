#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma
#   - senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver 
#   - correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da 
#   - advinhação, onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai 
#   - tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga 
#   - a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no 
#   - final mostre quantos palpites foram necessários para vencer.

from os import system
import random
password = 123
cont = 0

senha = int(input("Digite a sua senha: "))
while senha != password:
    senha = int(input("Senha digitada inválida!!! Tente novamente: "))
    system("cls")
print("Senha correta!!! Acesso liberado!!!")
print("=" * 80)
print("Seja bem vindo ao jogo da ADIVINHAÇÃO!!!")
num = random.randint(0,10+1)
numEscolhido = int(input("Digite um número para tentar adivinhar qual o computador pensou: "))

while numEscolhido != num:
    if num < numEscolhido:
        print("O número escolhido é MENOR que o que o computador pensou:")
    else:
        print("O número escolhido é MAIOR que o que o computador pensou: ")
    numEscolhido = int(input("Tente novamente: "))
    cont += 1
print(cont)