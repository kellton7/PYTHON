#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão

print(' ')
print('  10 TERMOS DE UMA PA  ')
print(' ')

termoInical = int(input('Digite o primeira termo de sua PA: '))
razao = int(input('Razão da PA: '))
decimo = termoInical + (10 - 1) * razao
for pa in range(termoInical, decimo + razao, razao):
    print(f'{pa}', end= ' -> ')
print('FIM!')