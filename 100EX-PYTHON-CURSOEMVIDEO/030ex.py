#Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar
n = int(input('Digite um numero: '))
div = n % 2
if div == 0:
    print(f'O numero {n} e PAR')
else:
    print(f'O numero {n} e IMPAR')