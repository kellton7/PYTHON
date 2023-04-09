#Faça um programa que leia um comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcule e mostre o comprimto da hiptenusa
from math import hypot
cateto_o = float(input('Digite o cateto oposto: '))
cateto_ad = float(input('Digite o cateto adjacente: '))
hip = hypot(cateto_o, cateto_ad)
print(f'O comprimento da hiptenusa é = {hip:.2f}')



