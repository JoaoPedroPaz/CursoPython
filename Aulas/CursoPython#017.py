num=[2, 5, 9, 1]
num[2]=3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.\n')

valores=list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for z, v in enumerate(valores):
    print(f'Na posição {z} encontrei o valor {v}')
print('Cheguei ao final da lista.\n')

a=[2, 3, 4, 7]
b=a #Ligação entre a e b
c=b[:] #Cópia de cada elemento de b para c
b[2]=8
print(f'Lista a: {a}')
print(f'Lista b: {b}')
print(f'Lista c: {c}')