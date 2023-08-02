#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

resultados = {}
ranking = {}

resultados['JAGAROR1'] = randint(1, 6)
resultados['JAGAROR2'] = randint(1, 6)
resultados['JAGAROR3'] = randint(1, 6)
resultados['JAGAROR4'] = randint(1, 6)

print('VALORES SORTEADOS')
print()

for k, v in resultados.items():
    print(f'{k} TIROU O NÚMERO {v} NO DADO.')
    sleep(1)

ranking = sorted(resultados.items(), key= itemgetter(1), reverse=True)

print()
print('RANKING DOS JOGADORES')
print()

for i, v in enumerate(ranking):
    print(f'{i+1} LUGAR: {v[0]} COM {v[1]}')
    sleep(1)