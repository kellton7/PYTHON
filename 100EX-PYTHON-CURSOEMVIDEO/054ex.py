#Crie um programa que leia o ano de nascimento de sete pessoas, no final, mostre quantas pessoas ainda não atigiram a marioridade e quantas ja
#são maiores
from datetime import date

atual = date.today().year
jovem = 0
velho = 0
for i in range(1, 8):
    dataNascimento = int(input(f'Digite o ano de nascimento da {i}º pessoa: '))
    idade = atual - dataNascimento
    if idade <= 18:
        jovem += +1
    else:
        velho += +1
print(f'Tivemos {jovem} pessoas menores de idade!')
print(f'E também {velho} pessoas maiores de idade!')
