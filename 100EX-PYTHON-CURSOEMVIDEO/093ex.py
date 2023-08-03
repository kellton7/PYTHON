#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele
#jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o 
#total de gols feitos durante o campeonato.

tabela = dict()
partidas = list()

print()
tabela['NOME'] = str(input('QUAL O NOME DO JODAGOR: ')).upper()
partida = int(input(f'QUANTAS PARTIDAS {tabela["NOME"]} JOGOU: '))
totalgols = 0

for c in range(0, partida):
    partidas.append(int(input(f'QUANTIDADE DE GOL NA {c + 1} PARTIDA: ')))
tabela['GOLS'] = partidas[:]
tabela['TOTAL'] = sum(partidas)

print()
print(tabela)
print()

print(f'O JOGADOR(A) {tabela["NOME"]} EM SUA {partida} PARTIDAS FEZ:')
print()

for c, k in enumerate(partidas):
    print(f' -= NA {c + 1} PARTIDA FEZ UM TOTAL DE {k} GOLS MARCADOS')




