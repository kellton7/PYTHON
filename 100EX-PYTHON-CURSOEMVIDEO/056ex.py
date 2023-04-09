#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final mostre a media de idade do grupo
#qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos
mediaIdade = 0
homemaisVelho = 0
nomeHomemvelho = ''
mulher20 = 0
for p in range (1, 5):
    print(f'{p}ª PESSOA!')
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual seu sexo[M/F]: ')).strip().upper()
    mediaIdade += idade
    if p == 1 and sexo == 'M':
        homemaisVelho = idade
        nomeHomemvelho = nome
    if sexo in 'M' and idade > homemaisVelho:
        homemaisVelho = idade
        nomeHomemvelho = nome
    if sexo in 'F' and idade < 20:
        mulher20 += +1
print(f'A média do grupo é {mediaIdade/4}')
print(f'O Homem mais velho tem {homemaisVelho} anos é seu nome é {nomeHomemvelho}')
print(f'Ao todo tem {mulher20} mulheres com menos de 20 anos')