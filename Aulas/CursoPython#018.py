teste=list()
teste.append('Gustavo')
teste.append(40)
galera=list()
galera.append(teste[:])
teste[0]='Maria'
teste[1]=22
galera.append(teste[:])
print(galera)

print('-='*30)

garela=[['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(garela[2][1])
for p in garela:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('-='*30)

galare=list()
dado=list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galare.append(dado[:])
    dado.clear()
print(galare)

print('-='*30)

totmai=0
totmen=0
for p in galare:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade.')
        totmai+=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen+=1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')