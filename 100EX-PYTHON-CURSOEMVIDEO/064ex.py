#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
#valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = next = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma = soma + num
    next += 1
print(f'Fim do Programa, Você digitou {next} números! E a soma deles é {soma}')