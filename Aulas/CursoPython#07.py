print(5+3*2)#11
print(5**2)#25
print(5**3)#125
print(19//2)#9
print(19/2)#9.5
print(365**522)#32875717981981342289734219608076461210798...
print(18%2)#0
print(122%3)#2
print(4**3)#64
print(pow(4,3))#64
print(81**(1/2))#9.0
print(25**(1/2))#5.0
print(127**(1/3))#5.026525695313479
print("Oi"+"Olá")#OiOlá
print("Oi"*5)#OiOiOiOiOi
print("="*20)#====================

nome=input("Qual é seu nome? ")
print("Prazer em te conhecer {:=^20}!".format(nome))

n1=int(input("Um valor: "))
n2=int(input("Outro valor: "))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print("A soma é {}, \no produto é {} e\n a divisão é {:.3f}".format(s, m, d), end =" >>> ")
print("Divisão inteira {} e potência {}".format(di, e))