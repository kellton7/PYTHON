#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela dua porção inteira
#ex: DIGITE UM NÚMERO: 6.127 0 NUMERO 6.127 TEM A PARTE INTEIRA 6

from math import trunc

num = float(input('Digite um numero: '))
fat = trunc(num)
print(f'O número {num} tem a parte inteira de {fat}')



