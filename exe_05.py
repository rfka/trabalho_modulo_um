#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento 
#   - necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade 
#   - de letras foram retiradas da frase original.

aux = 0
def tiraVogais(frase):
    aux = 0
    for cont in frase:
        if cont in "aeiouàáâãéêíóõôú":
            aux +=1
    for i in "aeiou":
        frase = frase.replace(i, " ")

    return(aux,frase)


frase = str(input("Digite uma frase: ").lower())
aux, fraseOK = tiraVogais(frase)

print(f"A quantidade de vogais contida na frase é: {aux}")
print(f"A frase sem as vogais ficou assim: {fraseOK}")
