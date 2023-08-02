#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a 
#CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com 
#quantos anos a pessoa vai se aposentar.

from datetime import datetime

cadastro = {}

cadastro['NOME'] = str(input('DIGITE O SEU NOME: '))
ANONASCIMENTO = int(input('SEU ANO DE NASCIMENTO: '))
cadastro['CARTEIRA'] = int(input('CARTEIRA DE TRABALHO (0 NÃO TEM): '))

cadastro['IDADE'] = datetime.now().year - ANONASCIMENTO

if cadastro['CARTEIRA'] != 0:
    cadastro['ANOCONTRATACAO'] = int(input('QUAL SEU ANO DE CONTRATAÇÃO: '))
    cadastro['SALARIO'] = float(input('SALÁRIO: R$'))
    cadastro['APOSENTADORIA'] = cadastro['IDADE'] + ((cadastro['ANOCONTRATACAO'] + 35) - datetime.now().year)

print()
for k, v in cadastro.items():
    print(f'{k} TEM O VALOR {v}')


