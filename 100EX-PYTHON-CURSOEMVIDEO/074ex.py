#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla, depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
from random import randint
menorValor = 0
maiorValor = 0
tupla = (randint(0,11),randint(0,11),randint(0,11),randint(0,11),randint(0,11))
print(f'Lista de números gerados aleatótiamente: {tupla}')
print(f'O maior valor sorteado é: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')
