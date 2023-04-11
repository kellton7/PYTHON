#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivso preços na sequência. No final mostre
#Uma lista de preços, organizando os daods em forma tabular
Contagem = ('Maminha', 54.99, 'Picanha', 119.99,
            'Azeite', 31, 'Tempero', 2, 'Lasanha', 16,
            'Amendoim', 3, 'Chocolate', 7, 'Oreo', 7)
print('-'*40)
print(f'{"LISTA DE COMPRAS":^40}')
print('-'*40)
for item in range(0, len(Contagem)):
    if item % 2 == 0:
        print(f'{Contagem[item]:-<30}', end= ' ')
    else:
        print(f'R${Contagem[item]:>8.2f}')
print('-'*40)