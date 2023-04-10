#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por exrenso.

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quadro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',' Dez', 'Onze','Doze'
            ,'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um número entre 0 a 20: '))
while num not in range (0, 21):
    num = int(input('POR FAVOR! Digite um número entre 0 a 20: '))
print(f'O número digítado {num} por extenso é {contagem[num]}')
print('FIM DO PROGRAMA!')

