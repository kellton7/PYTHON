#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
#sua categoria de acordo com a idade, até 9 anos: Mirim, ate 14 anos: Infantil, ate 19: junior, ate 20 anos: Seniro, acima: master

from datetime import date
atual = date.today().year

datanascimento = int(input('Digite sua data de nascimento: '))
idade = atual - datanascimento

if idade <=9 :
    print(f'Sua categoria é MIRIM, com {idade} anos')
elif idade <= 14 :
    print(f'Sua categoria é INFANTIL, com {idade} anos')
elif idade <= 19:
    print(f'Sua categoria é JUNIOR, com {idade} anos')
elif idade <= 25:
    print(f'Sua categoria é SENIOR, com {idade} anos')
else:
    print(f'Sua categoria é MASTER, com {idade} anos')