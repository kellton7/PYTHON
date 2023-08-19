#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA TRÊS PARÃMETOS: INICIO, FIM E PASSO E REALIZE A CONTAGEM
#SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGEMS ATRAVÉS DA FUNÇÃO CRIADA: DE 1 ATÉ 10 DE 1 EM 1, DE 10 ATÉ 0 DE 2 EM 2, UMA CONTAGEM PERSONALIZADA
from time import sleep

def contador(inicio, fim, passo):
    
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print(f'CONTAGEM DE {inicio} ATÉ {fim} DE {passo} EM {passo}!')
    sleep(2)
    

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}' , end= ' ', flush=True) 
            sleep(0.5)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}' , end= ' ', flush=True)
            sleep(0.5)
            cont -= passo
        
        
    print()
    print('-'* 30)
    

contador(1, 10, 1)
contador(10, 0, 2)
print('AGORA É SUA VEZ, ESOLHA SUA CONTAGEM: ')
ini = int(input('INÍCIO DA CONTAGEM: '))
fim = int(input('FIM: '))
p = int(input('PASSO: '))
contador(ini, fim , p)
 