#Crie um programa que leia o nome e o preço de varios produtos. O Programa devera perguntar se o usuario vai continuar, no final mostre:
#qual é o total gasto na compra, quantos produtos custam mais de 1000, qual é o nome do produto mais barato!
totalgasto = mais1000 = menor =  cont = 0
barto = ''
while True:
    nome = str(input('QUAL O NOME DO PRODUTO: '))
    preco = float(input('QUAL O PREÇO DO PRODUTO: R$ '))
    cont += 1
    totalgasto += preco
    if preco >= 1000:
        mais1000 += 1
    if cont == 1: #or preco < menor:
        menor = preco
        barto = nome
    else:
        if preco < menor:
            menor = preco
            barto = nome
    print('-'*30)
    contin = ' '
    while contin not in 'SN':
        contin = str(input('QUER CONTINUAR [S/N]: ')).strip().upper()[0]
    if contin == 'N':
        break
print('-'*30)
print(f'TOTAL GASTO NA COMPRA R$ {totalgasto:.2f}')
print(f'{mais1000} PRODUTOS CUSTA MAIS DE R$ 1000')
print(f'O PRODUTO MAIS BARATO FOI {barto} QUE CUSTA R${menor:.2f}')
