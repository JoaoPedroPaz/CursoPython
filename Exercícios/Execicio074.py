from random import randint
numeros=(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("O valores sorteados foram: ", end="")
for n in numeros:
    print(f"{n} ", end="")
print(f"\nO maior valor serteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")