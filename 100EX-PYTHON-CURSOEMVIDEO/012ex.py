#Faça um algoritmo que leia o preço de um produto e mostre seu preço, com 5% de desconto

produto = float(input('Qual o preço do produto: R$'))
desconto = produto / 20

print(f'O produto com 5% de desconto vai ficar: R${produto - desconto:.2f}')

