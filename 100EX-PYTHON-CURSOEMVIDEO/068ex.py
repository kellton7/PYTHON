#Faça um programa que joque par ou impar com o computador. O jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias e
# consecutivas que ele conquistou no final do jogo

from random import randint
s = cout = 0
print(''' 
-----------------------------
VAMOS JOGAR PAR OU ÍMPAR
-----------------------------
''')
while True:
    escolha = ' '
    n = int(input('Digite um numero: '))
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    compu = randint(0, 10)
    s = n + compu
    print(f'Você jogou {n} e computador {compu}. Total {s}! ',end= '')
    print('DEU PAR!' if s % 2 == 0 else 'DEU ÍMPAR!')
    if escolha == 'P':
        if s % 2 == 0:
            print('-'*35)
            print('Parabens você VENCEU')
            print('VAMOS JOGAR NOVAMENTE')
            print('-'*35)
            cout += 1
        else:
            print('-'*35)
            print('VOCÊ PERDEU')
            print('-'*35)
            break
    elif escolha == 'I':
        if s % 2 != 0:
            print('-'*35)
            print('Parabens você VENCEU')
            print('-'*35)
            cout += 1
        else:
            print('-'*35)
            print('VOCÊ PERDEU')
            print('-'*35)
            break
    print('VAMOS JOGAR VOVAMENTE...')
print(f'GAME OVER! VOCÊ VENCEU {cout} VEZES')





