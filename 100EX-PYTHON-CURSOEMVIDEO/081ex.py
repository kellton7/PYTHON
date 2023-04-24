#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: Quantos números foram digitados
#A lista de valroes ordenada de forma decresente, Se o valor 5 foi digitado.
ListaValores = []
while True:
    escolha = ' '
    ListaValores.append(int(input('Digite um valor: ')))
    while escolha not in 'SN':
        escolha = str(input('QUER CONTINUAR[S/N]: ')).upper().strip()
    if escolha == 'N':
        break
print( )
print(f'NO TOTAL VOCÊ DIGITOU {len(ListaValores)}')
ListaValores.sort(reverse= True)
#print(f'OS VALOES EM ORDEM DECRESENTE: {sorted(ListaValores, reverse= True)}')
print(f'OS VALOES EM ORDEM DECRESENTE: {ListaValores}')
if ListaValores.count(5):
    print(f'O VALOR 5 ESTÁ NA LISTA NA {ListaValores.index(5)+1}ª POSIÇÃO')
else:
    print(f'O VALOR 5 NÃO ESTÁ NA LISTA')