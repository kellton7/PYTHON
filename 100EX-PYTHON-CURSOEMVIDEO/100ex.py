#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 
#números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função 
#anterior.

from random import randint
from time import sleep

def sorteia(l):
    print(f'SORTEANDO 5 NÚMEROS ALEATORIOS: ', end= ' ')
    for cont in range(0, 5):
        n = randint(0, 10)
        l.append(n)
        print(f'{n}', end= ' ', flush=True)
        sleep(0.5)
    print()


def somaPar(l):
    soma = 0
    for v in l:
        if v % 2 == 0:
            soma += v
    print(f'SOMANDO OS VALORES PARES DA LISTA: {numeros} TEMOS {soma}')        


numeros = list()
sorteia(numeros)
somaPar(numeros)
