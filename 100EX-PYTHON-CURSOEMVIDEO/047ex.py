#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

n = int(input('Mostre os números pares entre um intervalo de 1 á :'))
for cont in range(0, n+1, 2):
    print(cont, end=' ')
print('Fim')