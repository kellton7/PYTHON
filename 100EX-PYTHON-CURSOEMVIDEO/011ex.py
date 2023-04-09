# faça um programa que leia a largura e a altura de uma parede em em metros, calcule a sua area e quantidade
#de tinta necessaria para tintar, sabendo que cada litro de tinta pinta um area de 2m
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

print(f'A area da parede é: {largura * altura}, e vai ser necessario {(largura * altura) / 2 } litros de tinta para pintar')
