#SubRotina
def lin():
    print('-'*30)

#Programa Principal
lin()
print('     CURSO EM VIDEO      ')
lin()
print('     Aprenda Python      ')
lin()
print('     GUSTAVO GUANABARA      ')
lin()
print()

#SubRotina
def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

#Programa Principal
titulo('     CURSO EM VIDEO      ')
titulo('    Phyton é muito bom! ')
titulo('oi')
print()

#SubRotina
def soma(a, b):
    print(f'A={a} e B={b}')
    s=a+b
    print(f'A soma A+B={s}')

#Programa Principal
soma(4, 5)
soma(b=4, a=5)
soma(7, 2)
print()

#SubRotina
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    tam=len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

#Programa Principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print()

#SubRotina
def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1
        
#Programa Principal
valores=[6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)