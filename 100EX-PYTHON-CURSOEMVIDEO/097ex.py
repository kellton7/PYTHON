#FAÇA UM PROGRAMA QUE TENHA FUNÇÃO CHAMADA ESCREVA(), QUE RECEBA UM TEXTO QUALQUER COMO PARÃMETRO E MOSTRE UMA MENSAGEM COM TAMANHO ADAPTÁVEL

def mensagem(txt):
    
    tam = len(txt)  + 4
    print('-'* tam)
    print(f'  {txt}')
    print('-'* tam)


mensagem('kelton lima')
mensagem('hello')
mensagem('oi')


