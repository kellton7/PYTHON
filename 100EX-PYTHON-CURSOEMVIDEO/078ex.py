#Programa que leia 5 valores numeros e guarde-os em uma lista, no final mostre qual foi o maior e o menor valor digitado
#e suas respectivas posições na lista.
valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont+1}ª valor: ')))
print('-'*50)
print(f'Os valores digitados foi : {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f' {i}...',end='')
print()
print(f'O menor valor digitado foi {min(valores)} nas posuções', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f' {i}...', end='')

