#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e consição de pagamento:
# a vista dinheiro/cheque: 10% de desconto
#a vista no cartão; 5% de desconto
# em atr 2x no cartão; preço normal, 3x ou mais no cartão 20% de juros

produto = float(input('Digite qual o preço do produto: '))
print('''Escolha a forma de pagamento:
[ 1 ] Á vista dinheiro /cheque!
[ 2 ] Á vista no cartão!
[ 3 ] Até 2x no cartão!
[ 4 ] 3x ou mais no cartão!''')

opçao = int(input('Sua escolha: '))

if opçao == 1:
    print(f'O produto R$ {produto} vai ficar com 10 % de desconto, Total = R$ {produto - (produto * 10 / 100)}')
elif opçao == 2:
    print(f'O produto R$ {produto} vai ficar á vista no cartão com 5 % de desconto, Total = R$ {produto - (produto * 5 / 100)}')
elif opçao == 3:
    parcela = produto / 2
    print(f'O produto R$ {produto} vai ficar, ', end='')
    print(f'Parcelado em 2x de R$ {parcela}!')
elif opçao == 4:
    totalparc: int = int(input('Quantas parcelas? '))
    if totalparc <= 2:
        print('ERRO, TENTE NOVAMENTE!!')
    else:
        parcela = produto / totalparc
        agrec = produto + (produto * 20 / 100)
        print(f'O produto R$ {produto} vai ficar com 20 % de juros, Total = R$ {agrec}')
        print(f'parcelado em {totalparc}x vai ficar R$ {agrec/totalparc}')
else:
    print('Opção de escolha Invalida!')