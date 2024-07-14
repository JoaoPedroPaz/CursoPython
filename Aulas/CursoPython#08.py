import random
from math import sqrt, floor

num1 = random.randint(1, 10)
print(num1)

num2=int(input("Digite um número: "))
raiz=sqrt(num2)
print("A raiz de {} é igual a {:.2f}".format(num2, floor(raiz)))