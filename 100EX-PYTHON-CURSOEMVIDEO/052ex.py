#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))

cout = 0
for c in range(1, num+1):

    if num % c == 0:
        print('\033[97m', end='')
        cout += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')

print(f'\n\033[mO número {num} foi divisível {cout} vezes')
if cout == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Ele não é PRIMO!')
