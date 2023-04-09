#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input("Dígite uma frase: ")).strip().upper()
palavras = frase.split()
all = ''.join(palavras)
inverso = ''

for letra in range(len(all) - 1, -1, -1 ):
     inverso += all[letra]
print(f'O inverso de {all} é {letra}')
if inverso == all:
    print('Temos um palíndromo')
else:
    print('A frase não é palíndromo')

