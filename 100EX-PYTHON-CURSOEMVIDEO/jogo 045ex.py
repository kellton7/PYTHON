#Crie um programa que faça o computador jogar Jokenpõ com você

import random
from time import sleep

lista = ['PEDRA', 'PAPEL', 'TESOURA']
print(' ' * 10)
print('JOKENPÕ')
print(' ' * 10)
print('LOADING...'), sleep(2)
print('''O COMPUTADOR ESCOLHEU UMA DAS 3 ALTERNATIVAS A SEGUIR!!!

    [ 0 -  PEDRA  ]
    [ 1 -  PAPEL  ]
    [ 2 - TESOURA ]
''')
escolha = random.randint(0, 2)
user = int(input('AGORA É SUA VEZ! ESCOLHA UMA DAS 3 ALTERNARTIVAS ACIMA E GANHE DO COMPUTADOR: '))
print(' ' * 10)
print('LOADING...'), sleep(2)
print(' ' * 10)
if escolha == 0: # PEDRA
    if user == 0:
        print('EMPATE!')
    elif user == 1:
        print('JOGADOR VENCE!')
    elif user == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA')

elif escolha == 1:  # PAPEL
    if user == 0:
        print('COMPUTADOR VENCE!')
    elif user == 1:
        print('EMPATE!')
    elif user == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA')

elif escolha == 2:  # TESOURA
    if user == 0:
        print('JOGADOR VENCE!!')
    elif user == 1:
        print('COMPUTADOR VENCE!')
    elif user == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA')

print(f'O computador jogou {escolha}')
print(f'O user jogou {user}')
print(' ' * 10)





