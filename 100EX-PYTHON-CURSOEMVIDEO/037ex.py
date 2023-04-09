#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
#a base de conversão: 1- para binario 2- para octal 3- para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para fazer a conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] pra hexadecimal ''')
opção = int(input('Sua escolha: '))

if opção == 1:
    print(f'{num} convertido para BINÁRIO é: {bin(num)[2:]} ')
elif opção == 2:
    print(f'{num} convertido para OCTAL é: {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é: {hex(num)[2:]}')
else:
    print('Ops! Você escolheu um número errado, tente novamente!')
