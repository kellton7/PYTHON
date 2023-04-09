#Refaça o desafio 035 dos trinagulos acrecentando o recurso de mostrar que tipo de tringulo sera formado:
#Equilátero: todos os lados iguais, Isósceles: dois lados iguais, Escaleno: Todos os lados diferentes

r1 = float(input('Qual o tamanho da 1 reta: '))
r2 = float(input('Tamanho da 2 reta: '))
r3 = float(input('Tamanho da 3 reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Voce pode fazer um triangulo, ', end='')

    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')

else:
    print('Voce NÂO pode fazer um triangulo')

