pessoas={'nome': 'gustavo',
         'sexo': "m",
         'idade': 22}
pessoas['peso']=98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()

brasil=[]
estado1={'uf': 'Rio de Janeiro', 'sigla': "RJ"}
estado2={'uf': 'saopaulo', 'sigla': 'sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])

print()

estado=dict()
brasil=list()
for c in range(0, 3):
    estado['uf']=str(input('Unidade Federativa: '))
    estado['sigla']=str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()