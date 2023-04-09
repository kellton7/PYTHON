#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome

nome = str(input('Digite seu nome completo: ')).upper().strip()
print(f'Voce tem silva no seu nome? {"SILVA" in nome}' )
