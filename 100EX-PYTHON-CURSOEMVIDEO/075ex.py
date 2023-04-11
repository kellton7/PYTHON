#Desenvolva um prgrama que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre
#Quantas vezes apareceu o valor 9,  em qual posição foi digirado o primeiro valor 3, quais foram os numeros pares
num = (int(input('Digite um valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite mais um valor: ')),
    int(input('Digite o último valor: ')))
print(f'Os valore que você digitou foi: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if num.count(3):
    print(f'O valor 3 está na posição: {num.index(3)+1}ª')
else:
    print('O valor 3 não apareceu nenhuma vez')
print(f'Os numeros pares digitados são: ', end= '')
for n in num:
    if n % 2 == 0:
        print(n, end= ' ')

