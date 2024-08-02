print("-="*20)
print("Analisador de triangulos")
print("-="*20)
r1=float(input("Primeiro seguimento: "))
r2=float(input("Segundo seguimento: "))
r3=float(input("Terceiro seguimento: "))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print("Os seguimentos acima PODEM formar um triangulo.")
else:
    print("Os seguimentos acima NÃO podem formar um triangulo.")
