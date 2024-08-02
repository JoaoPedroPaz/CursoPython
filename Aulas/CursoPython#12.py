nome=str(input("Qual é seu nome? "))
if nome=="Gustavo":
    print("Que nome bonito!")
elif nome=="Joao" or nome=="Pedro":
    print("Seu nome é bem popular no Brasil.")
elif nome in "Ana Claudia Jéssica Juliana":
    print("Belo nome feminino.")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia, {}".format(nome))