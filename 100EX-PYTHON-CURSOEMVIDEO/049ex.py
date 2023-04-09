# tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite o número para fazer a tabuada do mesmo: '))
for t in range (1, 11):
    print(f'{num} * {t} = {num * t}')
