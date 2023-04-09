#REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAÇÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PA USANDO WHILE

print(' ')
print('  10 TERMOS DE UMA PA  ')
print(' ')

termoInical = int(input('Digite o primeiro termo de sua PA: '))
razao = int(input('Razão da PA: '))
termo = termoInical
cout = 1
while cout <= 10:
    print(f'{termo}', end= ' -> ')
    termo += razao
    cout +=1
print('FIM!')