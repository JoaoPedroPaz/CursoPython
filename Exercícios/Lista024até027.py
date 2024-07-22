#Exercício Python #024 - Verificando as primeiras letras de um texto
print("Exercício Python #024 - Verificando as primeiras letras de um texto")
cid=str(input("Em que cidade você nasceu? ")).strip()
print(cid[:5].upper()=="SANTO")

#Exercício Python #025 - Procurando uma string dentro de outra
print("\nExercício Python #025 - Procurando uma string dentro de outra")
nome=str(input("Qual é seu nome completo? ")).strip()
print("Seu nome tem Silva? {}".format("silva" in nome.lower()))

#Exercício Python #026 - Primeira e última ocorrência de uma string
print("\nExercício Python #026 - Primeira e última ocorrência de uma string")
frase=str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase.".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A última letra A apareceu na posição {}".format(frase.rfind("A")+1))

#Exercício Python #027 - Primeiro e último nome de uma pessoa
print("\nExercício Python #027 - Primeiro e último nome de uma pessoa")
n=str(input("Digite o seu nome completo: ")).strip()
nome=n.split()
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}.".format(nome[0]))
print("Seu último nome é {}.".format(nome[len(nome)-1]))