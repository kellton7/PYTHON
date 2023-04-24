#Crie um programa que vai ter ler vários números e colocar em uma lista, depois disso crie duas listas extras que vão conter apenas
#os valores pares e os valores impares digitados reséctivamente. ao final mostre o conteúdo das tres listas geradas.

listaCompleta = []
listaPares = []
listaImpares = []
while True:
    continuar = ' '
    num = int(input('Digite um valor: '))
    listaCompleta.append(num)
    if num % 2 == 0:
        listaPares.append(num)
    else:
        listaImpares.append(num)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print( )
print(F'A LSSTA COMPLETA: {listaCompleta}')
print(f'A LISTA COM NÚMEROS PARES: {listaPares}')
print(f'A LISTA COM NÚMEROS IMPARES: {listaImpares}')
