#Melhore o jogo do desafio 028 onde um computador vai 'Pensar' e um numero, so que agora o jogador vai tentar adivinhar
#até acertar, mostrando no final quantos palpites foram necessários para vecer

from random import randint
from time import sleep


palpites = 0
compu = randint(0, 10)
acertou = False
print(' ' * 20)
print('O computador escolheu um número entre 0 e 10!')
while not acertou:
    jogador = int(input('Qual você acha que foi: '))
    palpites += 1
    print('PROCESSANDO...'), sleep(1)
    print(' ')
    if jogador == compu:
        acertou = True
    else:
        if jogador < compu:
            print('MAIS...TENTE NOVAMENTE: ')
        elif jogador > compu:
            print('MENOS...TENTE NOVAMENTE: ')
print(f'Parabens o número escolhido foi {compu}, voçê acertou!!!')
print(f'FIM, a quantidade de palpites foi de {palpites} ')


