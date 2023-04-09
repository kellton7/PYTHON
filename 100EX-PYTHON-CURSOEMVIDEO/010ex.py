#CRIE UM PROGRAMA QUE LEIA QUANDO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR
# DOLAR :  3.37

dinheiro = float(input('Quantos de reais voçe tem? R$ '))
trasformar = dinheiro/ 5.35

print(f'Voce tem:  {dinheiro} e pode comprar: US${trasformar:.2f} dolar')
