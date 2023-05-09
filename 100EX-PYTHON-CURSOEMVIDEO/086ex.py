#Programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz na tela. com a formatação correta
matriz = [[0, 0, 0], [0, 0 ,0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('DIGITE O VALOR PARA [{linha}, {coluna}] '))

print('-'*40)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}] ', end =' ')
    print()
    