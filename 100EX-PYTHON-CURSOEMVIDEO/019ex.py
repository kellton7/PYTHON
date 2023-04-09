# Um professor quer soltar um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
#ele, lendo o nome deles e escrevendo o nome escolhido

import random
n1 = input('Digite o nome do aluno 1: ')
n2 = input('Digite o nome do aluno 2: ')
n3 = input('Digite o nome do aluno 3: ')
n4 = input('Digite o nome do aluno 4: ')
lista = [n1, n2, n3, n4]
sorteio = random.choice(lista)
print(f'O aluno sorteado foi: {sorteio}')

