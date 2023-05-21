#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear
#6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista compotas
from random import randint
from time import sleep
lista = []
jogos = []
print('-'*55)
print('                 JOGO DA MEGA SENA       ')
print('-'*55)
jogo = int(input('QUANTOS JOGOS VOCÊ QUER: '))
print()
totalJogos = 1
while totalJogos <= jogo:  
    cont = 0 
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totalJogos += 1
print('-'* 5,f'SORTEANDO {jogo} JOGOS', '-'* 5)
print()
for i , l in enumerate (jogos):
    print(f'JOGO {i+1}: {l}')    
    sleep(1)
print('-='* 5, 'BOA SORTE', '-='*5)
