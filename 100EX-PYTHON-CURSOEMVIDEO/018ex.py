#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, consseno e tangente desse angulo

from math import sin,cos,tan, radians
an = float(input('Digite um angulo: '))
seno = sin(radians(an))
print(f'O angulo de {an} tem o SENO de {seno:.2f}')
cos = cos(radians(an))
print(f'O angulo de {an} tem o CONSSENO de {cos:.2f}')
tan = tan(radians(an))
print(f'O angulo de {an} tem a TANGENTE de {tan:.2f}')



