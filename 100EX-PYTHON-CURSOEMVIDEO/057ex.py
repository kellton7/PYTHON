#Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'. Caso os esteja errado, peça
#a digitação novamente até um valor correto.

sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Por Favor, informe seu sexo: [M/F] '))
print(f'Sexo {sexo} foi adicionado! FIM')