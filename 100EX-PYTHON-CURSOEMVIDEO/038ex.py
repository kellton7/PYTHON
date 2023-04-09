#Escreva um programa que leia dois números inteiros e compare - os, mostrando na tela
# - O primeiro valor é maior - O segundo valoor é maior - Não existe valor maior, os dois são iguais

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

if num1 > num2:
    print(f'O PRIMEIRO valor {num1} é maior!')
elif num1 == num2:
    print(f'Os valores são iguais')
else:
    print(f'O SEGUNDO valor {num2} e maior!')
