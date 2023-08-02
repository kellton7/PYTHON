#FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO, GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONARIO.
#NO FINAL MOSTRE O CONTEÚDO DA ESTRURURA NA TELA

dic = {}

dic['NOME'] = str (input('DIGITE O NOME DO ALUMO: '))
dic['MEDIA'] = float(input(f'MÉDIA DE {dic["NOME"]}: '))

if dic['MEDIA'] >= 7:
    dic['SITUACAO'] = 'APROVADO'
elif 5 <= dic['MEDIA'] < 7:
    dic['SITUACAO'] = 'RECUPERAÇÃO'
else:
    dic['SITUACAO'] = 'REPROVADO'
print('-=-' * 35)
for c, v  in dic.items():
    print(f'{c} É IGUAL A {v}')