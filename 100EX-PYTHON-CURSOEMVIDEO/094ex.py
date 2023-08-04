#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os 
#dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D)
#Uma lista de pessoas com idade acima da média

cadastro = dict()
lista = list()
soma = media = 0
listaF = list()

while True:
    
    cadastro.clear()
    cadastro['NOME'] = str(input('QUAL SEU NOME: ')).upper()
    cadastro['IDADE'] = int(input('QUAL SUA IDADE: '))
    soma += cadastro['IDADE']

    while True:
        cadastro['SEXO'] = str(input('QUAL SEU SEXO(M \ F): ')).strip().upper()
        if cadastro['SEXO'] in 'MF':
            break
        print('ATENÇÃO! DIGITE APENAS "M" OU "F" ')

    lista.append(cadastro.copy())

    while True:
        next = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
        if next in 'SN':
            break
        print('ATENÇÃO! DIGITE APENAS "S" OU "N"')

    if next == 'N':
        break
media = soma / len(lista)

print()
print(f'TEMOS NO TOTAL DE {len(lista)} PESSOAS CADASTRADAS')
print(f'TEMOS UNA MEDIA TOTAL DE {media:5.2f} ANOS')

print(f'AS MULHERES CADASTRADAS FORAM ', end= ' ')
for p in lista:
    if p['SEXO'] in 'Ff':
        print(f'{p["NOME"]}')

print(f'AS PESSOAS ACIMA DA MÉDIA SÃO: ', end= ' ')
for p in lista:
    if p['IDADE'] >= media:
        print('   ')
        for k , v in p.items():
            print(f' {k} = {v}:', end= '')
print()
