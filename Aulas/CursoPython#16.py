lanches=("Hamburguer", "Suco", "Pizza", "Pudim", "Batata frita")

for cont in range(0, len(lanches)):
    print(f"Eu vou comer {lanches[cont]} na posição {cont}")
for comida in lanches:
    print(f"Eu vou comer {comida}")
for pos, comida in enumerate(lanches):
    print(f"Eu vou comer {comida} na posição {pos}")

print("Comi pra caramba!")

a=(2, 5, 4)
b=(5, 8, 1, 2)
c=b+a
print(c)
print(len(c))
print(c.count(5))
print(c.index(5, 1))

pessoa=("Gustavo", 39, "M", 99.88)
print(pessoa)
del(pessoa)