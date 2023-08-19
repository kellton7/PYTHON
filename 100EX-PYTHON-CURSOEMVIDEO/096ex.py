#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMDA AREA(), QUE RECEBA AS DIMENDSÕES DE UM TERRENO RETAMGULAR (LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO.

def area(lar, com):
    a = l * c
    print(f'A ÁREA DO TERRENO {l}x{c} É DE {a}M²')


print('CONTROLE DE TERRENOS')
print('-'*30)
l = float(input('LARGURA: '))
c = float(input('COMPRIMENTO: '))
area(l,c)
