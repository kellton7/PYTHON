#Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu Status de acordo com a tabela abaixo
'''
Abaixo de 18.5 : abaixo do peso     25 ate 30: sobrepeso    acima de 40: obsidade morbida
Entre 18;5 e 25: peso ideal         30 ate 40 : Obesidade
'''

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Você está abaixo do peso Ideal, IMC = {imc:.2f}')
elif 18.5 <= imc < 25 :
    print(f'Você está no peso Ideal, IMC = {imc:.2f}')
elif 25 <= imc < 30 :
    print(f'Você está em sobrepeso, IMC = {imc:.2f}')
elif 30 <= imc < 40:
    print(f'Você está em obesidade, IMC = {imc:.2f}')
else:
    print(f'Você está em obsidade morbida, IMC = {imc:.2f}')

