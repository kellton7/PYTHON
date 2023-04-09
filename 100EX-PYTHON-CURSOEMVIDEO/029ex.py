#Escreva um programa que leia a velocidade de um carro. Se le ultrapassar 80 km mostre uma mensagem dizendo que le foi multado
# a multa e de 7 reias po cada km acima do limite

vel = float(input('Em qual veclocidade voçe está: '))
m = (vel - 80) * 7
if vel <= 80:
    print(f'Voce esta no velocidade {vel}km, permitida na via')
else:
    print(f'MULTADO!! Voce esta acima da velocidade permitida de 80km/H, sua multa é de {m} R$')
print(f'BOM DIA!')

