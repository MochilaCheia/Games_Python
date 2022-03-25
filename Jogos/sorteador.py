import random

def sorteador():
    possiveis_desenhos = ['1h', '2hg', '3jgd']
    sorteio = input('Quer sortear seu desenho?')
    while sorteio != 'não':
        numeros_sortidos = random.choice(possiveis_desenhos)
        print(numeros_sortidos)
        possiveis_desenhos.remove(numeros_sortidos)
        sorteio = input('Deseja continuar sorteando?')


def sorteio():
    numeros_sortidos = [
        ''
    ]
    pass
    

if __name__=='__main__':
    print(sorteador())