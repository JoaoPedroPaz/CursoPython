#Exercício Python #005 - Antecessor e Sucessor
print("Exercício Python #005 - Antecessor e Sucessor")
n5=int(input("Digite um número: "))
print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}.".format(n5, (n5-1), (n5+1)))

#Exercício Python #006 - Dobro, Triplo, Raiz Quadrada
print("\nExercício Python #006 - Dobro, Triplo, Raiz Quadrada")
n6=int(input("Digite um número: "))
print("O dobro de {} vale {}.".format(n6, (n6*2)))
print("O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.".format(n6, (n6*3), n6, (n6**(1/2))))

#Exercício Python #007 - Média Aritmética
print("\nExercício Python #007 - Média Aritmética")
n7_1=float(input("Primeira nota: "))
n7_2=float(input("Segunda nota: "))
media=(n7_1+n7_2)/2
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}.".format(n7_1, n7_2, media))

#Exercício Python #008 - Conversor de Medidas
print("\nExercício Python #008 - Conversor de Medidas")
medida=float(input("Uma distância em metros: "))
cm=medida*100
mm=medida*1000
print("A medida de {}m corresponde a {:.0f}cm e {:.0f}mm.".format(medida, cm, mm))

#Exercício Python #009 - Tabuada
print("\nExercício Python #009 - Tabuada")
n9=int(input("Digite um número para ver sua tabuada: "))
print("-"*12)
print("{} x {:2} = {}".format(n9, 1, n9*1))
print("{} x {:2} = {}".format(n9, 2, n9*2))
print("{} x {:2} = {}".format(n9, 3, n9*3))
print("{} x {:2} = {}".format(n9, 4, n9*4))
print("{} x {:2} = {}".format(n9, 5, n9*5))
print("{} x {:2} = {}".format(n9, 6, n9*6))
print("{} x {:2} = {}".format(n9, 7, n9*7))
print("{} x {:2} = {}".format(n9, 8, n9*8))
print("{} x {:2} = {}".format(n9, 9, n9*9))
print("{} x {:2} = {}".format(n9, 10, n9*10))
print("-"*12)

#Exercício Python #010 - Conversor de Moedas
print("\nExercício Python #010 - Conversor de Moedas")
real=float(input("Quanto dinheiro você tem na carteira? R$"))
dolar=real/5.42
print("Com R${:.2f} você pode comprar US${:.2f}.".format(real, dolar))

#Exercício Python #011 - Pintando Parede
print("\nExercício Python #011 - Pintando Parede")
larg=float(input("Largura da parede: "))
alt=float(input("Altura da parede: "))
área=larg*alt
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(larg, alt, área))
tinta=área/2
print("Para pintar essa parede, você precisará de {}l de tinta.".format(tinta))

#Exercício Python #012 - Calculando Descontos
print("\nExercício Python #012 - Calculando Descontos")
preço=float(input("Qual é o preço do produto? R$"))
novo=preço-(preço*5/100)
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.".format(preço, novo))

#Exercício Python #013 - Reajuste Salarial
print("\nExercício Python #013 - Reajuste Salarial")
salario=float(input("Qual é o salário do funcionário? R$"))
novoSal=salario+(salario*15/100)
print("Um funcionário que ganhava R${:.2f}, com 15%' de aumento, passa a receber R${:.2f}.".format(salario, novoSal))

#Exercício Python #014 - Conversor de Temperaturas
print("\nExercício Python #014 - Conversor de Temperaturas")
c=float(input("Informe a temperatura em °C: "))
f=9*c/5+32
print("A temperatura de {}°C corresponde a {}°F.".format(c, f))

#Exercício Python #015 - Aluguel de Carros
print("\nExercício Python #015 - Aluguel de Carros")
dias=int(input("Quantos dias alugados? "))
km=float(input("Quantos km rodados? "))
pago=(dias*60)+(km*0.15)
print("O total a pagar é de R${:.2f}.".format(pago))