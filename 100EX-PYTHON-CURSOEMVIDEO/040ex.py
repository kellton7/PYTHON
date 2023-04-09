#Crie um programa que leia duas notas de um alunos e calcule sua média, mostrando uma mensagem no final
#de acordo com a média atingida:
#- media abaixo de 5.0 reprovado, ente 5.0 e 6.9 recuperação, media 7.0 ou superior aprovado

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

if 7 > media >=5 :
    print(f'Você está de RECUPERAÇAO com a média {media}')
elif media < 5:
    print(f'Você foi REPROVADO com a média {media}')
else:
    print(f'Parabens você foi APROVADO com a média de {media}')
