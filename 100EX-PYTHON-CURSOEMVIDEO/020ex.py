#O professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos faça um programa
#que leia o nome dos quadro alunos e mostre a ordem sorteada

import random
n1 = str(input('Digite o nome do aluno 1: '))
n2 = str(input('Digite o nome do aluno 2: '))
n3 = str(input('Digite o nome do aluno 3: '))
n4 = str(input('Digite o nome do aluno 4: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem será: ')
print(lista)




