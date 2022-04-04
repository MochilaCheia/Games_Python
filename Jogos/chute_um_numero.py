import random
from time import sleep

def chute_um_numero():
    print('>> Bem vindo! <<')
    print('Esse é um jogo onde vamos escolher um número entre 1 e 100'
          '\ne você terá de chutar um número e tentar adivinhar qual é, boa sorte jogador!')

    numero_aleatorio = random.randrange(1, 100)

    tentativa = int(input('Qual número você acha que é? \n'))
    # o programa executa sempre de dentro para fora

    while numero_aleatorio != tentativa:
        if tentativa < 1 or tentativa > 100:
            print('Esse número não vale ein!')

        elif tentativa > numero_aleatorio:
            print('ops! você chutou muito alto!')

        else :print('Opa! o seu chute foi muito baixo.')
        sleep(0.1)
        tentativa = int(input('Vamos de novo! Qual número você acha que é? \n'))

    print('Na mosca, você acertou em cheio o número!\nMeus parábens, você venceu!!!')
