#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.
r1 = float(input('Qual o tamanho da 1 reta: '))
r2 = float(input('Tamanho da 2 reta: '))
r3 = float(input('Tamanho da 3 reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Voce pode fazer um triangulo')
else:
    print('Voce NÂO pode fazer um triangulo')