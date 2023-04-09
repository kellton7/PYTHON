#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMENTOS a MILIMETROS

m = float(input('Digite um valor em metros: '))
print(f'Convertido em centimentos é: {m*100:.0f}cm \nEm milimetros é: {m*1000:.0f}mm \nEm metros é: {m}m')
print(f'Convertido em decimetros é: {m*10:.0f}dm \nEm damometros é: {m/10:.2f}dm \nEm Hectómetros é: {m/100:.2f}hm ')
print(f'Convertido em Quilómetros é: {m/1000:.4f}km')
