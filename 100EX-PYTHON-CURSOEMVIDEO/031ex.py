#Desenvolva um programa que pergunte a distancia de uma viagem em km. calcule o preço da passagem.
#cobrando 0.50 por  km para viagem de ate 200 km e 0.45 para viagem mais longa
dis = float(input('Qual a distancia da viagem em km: '))
if dis <= 200:
    print(f'A passagem vai custar {0.50 * dis:.2f} R$, para percorrer {dis} Km')
else:
    print(f'A passagem vai custar {0.45 * dis:.2f} R$, para percorrer {dis} Km')