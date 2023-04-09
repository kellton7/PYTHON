# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
print('')
print('SEQUENCIA DE FIBONACCI!')
print('')
num = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
cout = 3
print('')
print(f'{t1} -> {t2}', end='')
while cout <= num:
    t3 = t2 + t1
    t1 = t2
    t2 = t3
    print(f'-> {t3}', end='')
    cout += 1
print(' - FIM')

