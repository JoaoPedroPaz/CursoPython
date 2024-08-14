def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    : return: sem retorno
    """
    c=i
    while c<=f:
        print(f'{c} ', end='')
        c+=p
    print('FIM!')

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s=a+b+c
    #print(f'A soma vale {s}')
    return s

def par(n=0):
    if n%2==0:
        return True
    else:
        return False

help(contador) 

r1=somar(3, 2, 5)
r2=somar(2, 2)
r3=somar(6)

print(f'Os resultados foram {r1} {r2} e {r3}')

num=int(input('\nDigite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')