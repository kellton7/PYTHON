#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final
#mostre quantas pessoas foram cadastradas, uma listagem com as pessoas mais pesadas, uma listagem com as pessoas mais leves
pessoas = []
cadastrados = []
maxp = minp = 0
while True:
    cont = ' '
    pessoas.append(str(input('DIGITE O NOME: ')).upper())
    pessoas.append(int(input('DIGITE O PESO DA PESSOA: ')))
    if len(cadastrados) == 0:
        maxp = minp = pessoas[1]
    else:
        if pessoas[1] > maxp:
            maxp = pessoas[1]
        if pessoas[1 < minp]:
            minp = pessoas[1]
    cadastrados.append(pessoas[:])
    pessoas.clear()
    while cont not in 'NS':
        cont = str(input('QUER CONTINUAR[S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('-'*50)
print(f'VOCÊ CADASTROU {len(cadastrados)} PESSOAS! ')
print(f'O MAIOR PESO FOI DE {maxp}KG. PESO DE ', end = '')
for p in cadastrados:
    if p[1] == maxp:
        print(f'[{p[0]}] ', end = '')
print()
print(f'O MENOR PESO FOI DE {minp}KG. PESO DE ', end ='')
for p in cadastrados:
     if p[1] == minp:
        print(f'[{p[0]}] ', end = '')

