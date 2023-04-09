#FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DIGITOS SEPARADOS

num = int(input('Digite um numero entre 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d} ')
print(f'Centena: {c}')
print(f'Milhar: {m}')

'''
if num <= 9999:
    print(f'O valor escolhido {num} tem Unidade: {} ')
else:
    print(f'O valor {num} e maior que o permitido, por favor escolher outro valor')
'''
