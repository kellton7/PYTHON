#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento
#de cada jogador.

tabela = dict()
GOLS = list()
time = list()

while True: 

    print()
    tabela.clear()
    GOLS.clear()
    tabela['NOME'] = str(input('QUAL O NOME DO JODAGOR: ')).upper()
    partida = int(input(f'QUANTAS PARTIDAS {tabela["NOME"]} JOGOU: '))
    totalgols = 0

    for c in range(0, partida):
        GOLS.append(int(input(f'QUANTIDADE DE GOL NA {c + 1} PARTIDA: ')))
    tabela['GOLS'] = GOLS[:] 
    tabela['TOTAL'] = sum(GOLS) 

    time.append(tabela.copy())

    while True:
        next = str(input('QUER CONTINUAR: (S/N)')).upper()[0].strip()
        if next in 'SN':
            break
        print('POR FAVOR APENAS "S" OU "N"!')
    if next == 'N':
        break

print()
print(f'cod.' ,end='')
for i in tabela.keys():
    print(f' {i:<14}', end='')
print()

print('-=' *21)

for k, v in enumerate(time):
    print(f' {k:>3}', end= '')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()

print('-=' *21)

while True:
    dados = int(input('MOSTRAR DADOS DE QUAL JOGADOR? (999 PARA PARAR!)'))
    if dados == 999: 
        break
    if dados >= len(time):
        print(f'ERRO!!!! NÃO EXISTE JOGADOR COM ESSE COD')
    else:
        print(f'  TABELA DO JOGADOR(A) {time[dados]["NOME"]}') 
        for i, g in enumerate(time[dados]['GOLS']):
            print(f'   NO {i + 1} JOGO FEZ {g} GOLS')
print('-=' *21)


