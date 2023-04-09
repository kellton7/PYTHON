#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
#O NOME COM TODAS AS LETRAS MAIUSCULAS
#O NOME COM TODAS AS LETRAS MINUSCULAS
#QUANTAS LETRAS AO TODO (SEM CONCIDERAR ESPAÇOES)
#QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input('Digite seu nome completo: ')).strip()
nomeseparado = nome.split()
print(f'O nome tem {len(nome)- nome.count(" ")} caracteres, seu nome em maisculo é: {nome.upper()}')
print(f'Seu nome em minusculo é: {nome.lower()}')
print(f'O seu primeiro nome "{nomeseparado[0]}" tem caracteres {len(nomeseparado[0])}')


