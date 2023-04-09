#Crie um programa  que leia dois valores e mostre um menu na tela: [1] somar [2] multiplicar [3] maior [4] novos numeros
#[5] sair do programa seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input('DIGITE O PRIMEIRO VALOR: '))
num2 = int(input('DIGITE O SEGUNDO VALOR: '))

escolha = 0
while escolha != 5:
    (print('''
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA
    '''))
    escolha = int(input('QUAL SUA ESCOLHA: '))
    if escolha == 0 :
        print('ESCOLHA UM NUMERO MAIOR QUE "0"')
    elif escolha > 5:
        print('ESCOLHA UM NUMERO MENOR QUE "6"')
    if escolha == 1:
        print(f'A SOMA DOS NUMEROS {num1} + {num2} = {num1 + num2}')
    elif escolha == 2:
        print(f'A MULTIPLICAÇÂO DOS NUMEROS {num1} * {num2} = {num1 * num2}')
    elif escolha == 3:
        if num1 > num2:
            print(f'O NUMERO {num1} É O MAIOR')
        elif num1 == num2:
            print(f'OS NUMEROS {num1} E {num2} SÃO IGUAIS')
        else:
            print(f'O NUMERO {num2} É O MAIOR')
    elif escolha == 4:
        num1 = int(input('DIGITE O PRIMEIRO VALOR: '))
        num2 = int(input('DIGITE O SEGUNDO VALOR: '))
print('FIM DO PROGRAMA!')