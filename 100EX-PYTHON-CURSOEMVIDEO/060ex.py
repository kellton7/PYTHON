#Faça um programa que leia um numero qualquer e mostre o seu fatorial

num = int(input('Digite número para calcular ser fatorial: '))
c = num
f = 1
print(f'{num}!')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

