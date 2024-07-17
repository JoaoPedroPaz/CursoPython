import math
import random

#Exercício Python #016 - Quebrando um número
print("Exercício Python #016 - Quebrando um número")
num=float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}.".format(num, math.trunc(num)))
print("O valor digitado foi {} e a sua porção inteira é {}.".format(num, int(num)))

#Exercício Python #017 - Catetos e Hipotenusa
print("\nExercício Python #017 - Catetos e Hipotenusa")
co=float(input("Comprimento do cateto oposto: "))
ca=float(input("Comprimento do cateto adjacente: "))
hi17_1=(co**2+ca**2)**(1/2)
hi17_2=math.hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi17_1))
print("A hipotenusa vai medir {:.2f}".format(hi17_2))

#Exercício Python #018 - Seno, Cosseno e Tangente
print("\nExercício Python #018 - Seno, Cosseno e Tangente")
angulo=float(input("Digite o angulo que voce deseja: "))
seno=math.sin(math.radians(angulo))
print("O angulo de {} tem o seno de {:.2f}".format(angulo, seno))
cosseno=math.cos(math.radians(angulo))
print("O angulo de {} tem o cosseno de {:.2f}".format(angulo, cosseno))
tan=math.tan(math.radians(angulo))
print("O angulo de {} tem a tangente de {:.2f}".format(angulo, tan))

#Exercício Python #019 - Sorteando um item na lista
print("\nExercício Python #019 - Sorteando um item na lista")
n1=str(input("Primeiro aluno: "))
n2=str(input("Segundo aluno: "))
n3=str(input("Terceiro aluno: "))
n4=str(input("Quarto aluno: "))
lista=[n1, n2, n3, n4]
escolhido=random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))

#Exercício Python #020 - Sorteando uma ordem na lista
print("\nExercício Python #020 - Sorteando uma ordem na lista")
lista=[n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem de apresentação será ")
print(lista)
