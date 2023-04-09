#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado

km = float(input('Quantos km voce percoreu com o carro? '))
dias = float(input('Quantos dias voce ficou com o carro? '))
print(f'Voce ficou {dias} dias com carro e percoreu {km}km, o total por dia fica R${dias * 60:.2f}')
print(f'E o total por Km percorido é: {km * 0.15}Km \n Total final fica R$ {(dias * 60) + (km * 0.15)}')
