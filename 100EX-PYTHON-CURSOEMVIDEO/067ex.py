#Faça um programa que mostre a tabuada de varios numeros, um de cada vez para cada valor digitado pelo usuario. O programa será interrompido
#quando o número solicitado for negativo.
cout = 0
while True:
    num = int(input('Quer saber a tabuada de qual valor: '))
    if num < 0:
        break
    print('-'* 35)
    for t in range(1, 11):
        print(f'{num} x {t} = {num * t}')
        t +=1
    print('-'*35)
print('FIM DO PROGRAMA!')
