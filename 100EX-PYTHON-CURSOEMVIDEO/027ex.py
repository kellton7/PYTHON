#Faça um programa que leia o nome completo de uma pessoa, mostrando em sequida o primeiro e o ultimo nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
print(f'O primeiro nome é: {div[0]} e o ultimo é {div[len(div) - 1]}')