from time import sleep
from datetime import date

#Exercício Python #046 - Contagem regressiva
print("Exercício Python #046 - Contagem regressiva")
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.1)
print("BUM! BUM! POOOW!")

#Exercício Python #047 - Contagem de pares
print("\nExercício Python #047 - Contagem de pares")
for n in range(2, 51, 2):
    print(n, end=" ")
print("Acabou!")

#Exercício Python #048 - Soma ímpares múltiplos de três
print("\nExercício Python #048 - Soma ímpares múltiplos de três")
soma=0
cont=0
for c in range(1, 501, 2):
    if c%3==0:
        soma+=c
        cont+=1
print("A soma de todos os {} valores solicitados é {}".format(cont, soma))

#Exercício Python #049 - Tabuada v.2.0
print("\nExercício Python #049 - Tabuada v.2.0")
num=int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print("{} x {:2} = {}".format(num, i, num*i))

#Exercício Python #050 - Soma dos pares
print("\nExercício Python #050 - Soma dos pares")
soma=0
cont=0
for i in range(1, 7):
    num=int(input("Digite o {} valor:".format(i)))
    if num%2==0:
        soma+=num
        cont+=1
print("Você informou {} números PARES e a soma foi {}".format(cont, soma))

#Exercício Python #051 - Progressão Aritmética
print("\nExercício Python #051 - Progressão Aritmética")
primeiro=int(input("Primeiro termo: "))
razao=int(input("Razão: "))
decimo=primeiro+(10-1)*razao
for i in range(primeiro, decimo+razao, razao):
    print("{} ".format(i), end="-> ")
print("Acabou!")

#Exercício Python #052 - Números primos
print("\nExercício Python #052 - Números primos")
num=int(input("Digite um número: "))
tot=0
for i in range(1, num+1):
    if num%i==0:
        print("\033[33m", end="")
        tot+=1
    else:
        print("\033[31m", end="")
    print("{} ".format(i), end="")
print("\n\033[mO número {} foi divisivel {} vezes.".format(num, tot))
if tot==2:
    print("E por isso ele é primo.")
else:
    print("E por isso ele não é primo.")

#Exercício Python #053 - Detector de Palíndromo
print("\nExercício Python #053 - Detector de Palíndromo")
frase=str(input("Digite uma frase: ")).strip().upper()
palavras=frase.split()
junto="".join(palavras)
inverso=""
inverso2=junto[::-1]
print("O inverso de {} é {}.".format(junto, inverso2))
for letra in range(len(junto) -1, -1, -1):
    inverso+=junto[letra]
if inverso==junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo. ")

#Exercício Python #054 - Grupo da Maioridade
print("\nExercício Python #054 - Grupo da Maioridade")
atual=date.today().year
totmaior=0
totmenor=0
for pess in range(1, 5):
    nasc=int(input("Em que ano a {}ª pessoa nasceu? ".format(pess)))
    idade=atual-nasc
    if idade>=21:
        totmaior+=1
    else:
        totmenor+=1
print("Ao todo tivemos {} pessoas maiores de idade.".format(totmaior))
print("E também tivemos {} pessoas menores de idade.".format(totmenor))

#Exercício Python #055 - Maior e menor da sequência
print("\nExercício Python #055 - Maior e menor da sequência")
maior=0
menor=0
for p in range(1, 5):
    peso=float(input("Peso da {}ª pessoa: ".format(p)))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print("O maior peso lido foi de {}Kg".format(maior))
print("O menor peso lido foi de {}Kg".format(menor))

#Exercício Python #056 - Analisador completo
print("\nExercício Python #056 - Analisador completo")
somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=""
totmulher20=0
for p in range(1, 5):
    print("---- {}ª PESSOA ----".format(p))
    nome=str(input("Nome: ")).strip()
    idade=int(input("Idade: "))
    sexo=str(input("Sexo [M/F]: ")).strip()
    somaidade+=idade
    if p==1 and sexo in "Mm":
        moiridadehomem=idade
        nomevelho=nome
    if sexo in "Mm" and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in "Ff" and idade<20:
        totmulher20+=1
mediaidade=somaidade/4
print("A média de idade do grupo é de {} anos.".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(totmulher20))