#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#se ele ainda se alista ao serviço militar se é a hora de se alistar.
#se ja passou do tempo do alistamento.
#seu programa tambem devera mostrar o tempo que falta ou tempo que falta ou tempo que passou do prazo
from datetime import date
atual = date.today().year

dataNascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - dataNascimento

print(f'Quem nasceu em {dataNascimento} tem {idade} anos em {atual}')

if idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Não esta na hora de você se Alistar!, seu alistamento vai ser á {saldo} anos, em {ano}')
elif idade == 18:
    print(f'Está na hora de você se Alistar!')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Ops! Você deveria ter se alistado no ano de {ano}!')