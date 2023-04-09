#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuario qual sera o valor a ser sacasdo(numero int)
# e o programa vai informar quantas cedulas de cada valor serao entregues. OBS: caixa tem cedulas de 50, 20, 10 e 1
from time import sleep
print('-'*30)
print('CAIXA ELETRONICO')
print('-'*30)
sacar = int(input('QUAL O VALOR A SER SACADO: R$'))
print('PROCESSANDO...'), sleep(1)
total = sacar
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'TOTAL DE {totalced} CÉDULAS DE R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('-'*30)
print('FIM DO SAQUE!')



