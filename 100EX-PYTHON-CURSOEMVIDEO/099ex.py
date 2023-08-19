#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que 
#analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(*núm):

    print('-'* 69)
    print(f'OS VALORES INFORMADOS FORAM: {núm} TOTAL DE {len(núm)} NÚMEROS!')
    sleep(2)
    print(f'O MAIOR VALOR INFORMADO FOI: {max(núm)} E O MENOR: {min(núm)}')


maior(3 ,4, 55,6 ,4 ,6)
maior(0, 2, 1 , 4)
maior(-3, 4, 6 ,3)