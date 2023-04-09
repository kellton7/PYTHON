#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
media = soma = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar S/N :')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} de números é a media entre eles é {media}')
print(f'O maior valor é {maior} é o menor é {menor}')
