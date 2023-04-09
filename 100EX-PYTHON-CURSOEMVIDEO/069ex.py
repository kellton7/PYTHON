#Crie um programa que leia a idade e sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuario quer ou nao
#continuar. No final mostre: quantas pessoas tem mais de 18 anos, quantos homen foram cadastrados, quantas mulheres tem menosde 20 anos
mais18 = homen = mulher20 = 0
print('-'*30)
print('CADASTRO DE PESSOAS')
print('-'*30)
while True:
    idade = int(input('Digite a Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if s == 'M':
        homen += 1
    if s == 'F' and idade < 20:
        mulher20 += 1
    print('-' * 30)
    next = ' '
    while next not in 'SN':
        next = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
    print('-' * 30)
    if next == 'N':
        break
print(F'TOTAL DE PESSOAS COM MAIS DE 18 ANOS: {mais18}!')
print(f'AO TODO TEM {homen} HOMENS CADASTRADOS!')
print(f'E TEMOS {mulher20} MULHERES COM MENOS DE 20 ANOS!')
print('FIM DO PROGRAMA')

