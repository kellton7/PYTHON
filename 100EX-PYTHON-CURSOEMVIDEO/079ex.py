#Crie um programa onde o usuário possa digitar vários valores numericos e cadastre-os em uma lista. Caso o número já
#exista lá dentro, ele não seá adicionado. No final serão exibidos todos os valores únicos digitados, em ordem crescente
cadastro = []
while True:
    conti = ' '
    n = int(input('Digite um valor: '))
    if n not in cadastro:
        cadastro.append(n)   
        print('Valor CADASTRADO com sucesso!')
    else:
        print('O VALOR JÁ ESTÁ NA LISTA!')
    while conti not in 'SN':
        conti = str(input('QUER CONTINUAR [S/N]: ')).strip().upper()[0]
    if conti == 'N':
        break
print()
print('-'*50)
print(f'Você digitou os valores {sorted(cadastro)}')
print()

