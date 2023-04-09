#Faça um programa que leia tres numeros e mostre qual é o maior e qual e o menor
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite mais um numero: '))
n3 = float(input('Digite outro numero: '))

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')


