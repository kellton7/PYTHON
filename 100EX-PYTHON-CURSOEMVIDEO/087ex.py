#Aprimore o desafio anterior, mostrando no final a soma de todos os valores pares digitados. a soma dos valores da terceira caluna e O maior
# valor da segunda linha
matriz = [[0, 0, 0], [0, 0 ,0], [0, 0 ,0]]
valoresPares = valoresTerceiracoluna = maiorValorsegundacoluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'DIGITE O VALOR PARA [{linha}, {coluna}] '))

print('-'*50)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}] ', end= ' ')
        if matriz[linha][coluna] % 2 == 0:
            valoresPares += matriz[linha][coluna]
    print()
    
print('-'* 50)
print(f'A SOMA DOS VALORES PARES DA SUA MATRIZ FOI DE: {valoresPares}')

for linha in range(0, 3):
    valoresTerceiracoluna += matriz[linha][coluna]
    
print(f'A SOMA DOS VALORES DA 3 COLUNA É DE : {valoresTerceiracoluna}')

for coluna in range(0, 3):
    if coluna == 0:
        maiorValorsegundacoluna = matriz[1][coluna]
    elif matriz[1][coluna] > maiorValorsegundacoluna:
        maiorValorsegundacoluna = matriz[1][coluna]
        
print(f'O MAIOR VALOR DA SEGUNDA LINHA É: {maiorValorsegundacoluna}')