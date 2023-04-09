#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NAO COM O NOME SANTO

city = str(input('Digite um nome de uma cidade: ')).strip().lstrip()
s = city.upper().split()
print(f'A cidade {city} tem santo no começo? ', 'SANTO' in s[0])




