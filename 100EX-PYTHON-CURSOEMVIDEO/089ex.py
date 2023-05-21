#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta, no final mostre um boletim contendo 
#média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
lista = []
boletim = []
while True:
    cont = ' '
    nome = str(input('NOME DO ALUNO: '))
    nota1 = float(input('1º NOTA: '))
    nota2 = float(input('2º NOTA: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    
    while cont not in 'NS':
        cont = str(input('QUER CONTINUAR[S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break

print('-=' * 55)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')

while True:
    print('-='* 55)
    next = int(input('MOSTRAR NOTAS DE QUAL ALUNO[999 INTERROMPER]: '))
    if next == 999:
        print('FINALIZANDO...')
        break
    if next <= len(lista) - 1:
        print(f'NOTAS DE {lista[next][0]} SÂO {lista[next][1]}')