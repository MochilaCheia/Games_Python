import random

jogar_dado = input('Olá, você gostaria de rolar o dado?\nDigite "sim" ou "não"\n')

while jogar_dado != 'não':
    if jogar_dado == 'sim':
        face_do_dado = random.randint(1, 6)
        print(face_do_dado)
        jogar_dado = input('Deseja jogar o dado novamente?\n')
    else:
        jogar_dado = input('acho que você digitou errado, tente novamente:\n')

print('vou estar esperando você mudar de idéia.')
