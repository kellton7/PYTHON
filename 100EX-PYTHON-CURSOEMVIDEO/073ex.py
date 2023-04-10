#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
# Apenas os 5 primeiros colocacos, Os últimos 4 colocados, Uma lista com os times em ordem alfabética, Em que posição está o time Flamengo
tabelaBrasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico Paranaense', 'Atlético Mineiro'
                     , 'Fortaleza', 'São Paulo', 'América Fc Sa', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba'
                     , 'Cuiabá Saf', 'Ceará', 'Atlético', 'Avaí', 'Juventude') 
print('''
DADOS DA TABELA DO BRASILEIRAÕ
''')
print(tabelaBrasileirao)
print('-'*100)
print(f'Os 5 primeiros colocados são: {tabelaBrasileirao[:5]}')
print('-'*100)
print(f'Os últimos 4 colocados são: {tabelaBrasileirao[16:]}')
print('-'*100)
print(f'Ordem alfabética dos nomes: {sorted(tabelaBrasileirao)}')
print('-'*100)
print(f'O time Flamengo está na posição: {tabelaBrasileirao.index("Flamengo")}')