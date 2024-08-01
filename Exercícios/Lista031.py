distancia=float(input("Qual é a distância da sua viagem em quilômetro? "))
print("Você está prestes a começar uma viagem de {}Km.".format(distancia))
preço=distancia*0.5 if distancia <= 200 else distancia*0.45
print("E o preço da sua passagem será de R${}".format(preço))