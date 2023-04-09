#Faça um programa que calcule a soma entre todos os números inpares que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.

soma = 0
next = 0
for cont in range (1, 501, 2):
    if cont % 3 == 0:
        print(cont)
        next += 1
        soma += cont
print(' ')
print(f'A soma dos números ({next}) multiplos 3 até 500 é: {soma}')
print(next)
