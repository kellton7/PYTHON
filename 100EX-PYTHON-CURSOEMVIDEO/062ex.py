#REFAÇA O DESAFIO 061, LENDO O PRIMEIRO TERMO E A RAÇÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PA USANDO WHILE
#e quando acabar ele vai perguntar se ele vai querer mostrar mais termos

print('GERADOR DE PA')
print(' ')
termoInical = int(input('Digite o primeiro termo de sua PA: '))
razao = int(input('Razão da PA: '))
termo = termoInical
cout = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cout <= total:
        print(f'{termo}', end= ' -> ')
        termo += razao
        cout +=1
    print('PAUSA')
    mais = int(input('Quantos temos você quer mostrar a mais: '))
print('FIM')

