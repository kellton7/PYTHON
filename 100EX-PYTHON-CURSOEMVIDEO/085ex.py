#Programa onde o usuario possa dogitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e
#impares, No final  mostre os valores em ordem crescente.
cadastro = [[], []]
for cont in range(1 ,8):
    num = (int(input(f'DIGITE O {cont}ª NUMERO: ')))
    if num % 2 == 0:
        cadastro[0].append(num)
    else:
        cadastro[1].append(num)
print('-'*40)
print(f'VALORES PARES DIGITADOS: {sorted(cadastro[0])}')
print(f'VALORES IMPARES DIGITADOS: {sorted(cadastro[1])}')