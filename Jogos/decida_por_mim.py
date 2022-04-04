
import random

def decida_por_mim():

    respostas = [
        'Sim, sim', 'Claro!', 'Não, com certeza e absolutamente não', 'Talvez', 'Isso não é óbvio?',
        'Siga seu coração', 'Vai lá!', 'Acho que deveria', 'Acho melhor não', 'Pensa bem',
        'Pergunta pra sua mãe, ela com certeza sabe', 'Vai logo!',
        'Hoje?', 'Talvez amanhã', 'SE JOGAAA', 'VAI COM TUDO',
        'SE VOCÊ NÃO FOR LOGO EU VOU!', 'Não tenha medo, vai lá', 'Depende muito, veja suas prioridades',
        'No seu lugar eu iria', 'No seu lugar eu faria', 'Antes tarde que nunca', 'GO, GO', 'Só se for agora',
        'Pode ter certeza disso', 'ISSO AÍ', 'ESSA É A ESCOLHA CERTA', 'Pensa bem a respeito', 'Sim', 'Não,'
        'Absolutamente sim', 'Com toda certeza', 'Deixa pra quarta-feira'
                ]

    print('Pergunta quantas vezes quiser e pra encerrar digite "sair".')
    pergunta = input('Faça uma pergunta e veja a resposta:\n')

    while pergunta != 'sair':
        agora = random.choice(respostas)
        print(agora)
        pergunta = input('Agora, faça mais uma pergunta se quiser e eu te darei uma resposta:\n')

# validação e tratamento de resposta

if __name__=='__main__':
