#CRIE UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS IMFORMAÇÕES POSSIVEIS SOBRE ELA.

tipo = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(tipo))
print(f'Ele é um numero: {tipo.isnumeric()}')
print(f'Ele é uma letra: {tipo.isalpha()}')
print(f'Ele tem numeros e letras: {tipo.isalnum()}')
print(f'Ele so tem espaços: {tipo.isspace()}')
print(f'Ele esta em maisculo {tipo.isupper()}')
print(f'Ele esta em minusculo {tipo.islower()}')
print(f'Ele e capitalizada {tipo.istitle()}')













