#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999 que é a condição de
#parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles
s = cont = 0
print('O Programa vai parar se digitar 999!')
while True:
    n = int(input('Digite um numero Inteiro: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foi digitados um total de {cont} valores e a soma entre eles foi: {s}')