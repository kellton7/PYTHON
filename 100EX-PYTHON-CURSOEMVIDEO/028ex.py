# JOGO DA ADVINHAÇÂO
from random import randint
from time import sleep

print(' ' * 20)
n = int(input('O computador escolheu um número entre 0 e 5, qual voçê acha que foi: '))
print('PROCESSANDO...'), sleep(2)
if n > 5:
    print('Dica: o número é menor que 6')
compu = randint(0, 5)
if n == compu:
    print(f'Parabens o número escolhido foi {compu}, voçê acertou!!!')
else:
    print(f'Tente novamente, o número escolhido foi {compu}, e voçê chutou o {n}')

