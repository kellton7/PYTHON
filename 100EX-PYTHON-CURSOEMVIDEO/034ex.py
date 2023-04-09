# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. -Para os inferiores ou iguais,
# o aumento é de 15%.

salario = float(input('Qual seu salario: '))
if salario >= 1250:
    print(f'Seu salario teve o aumento de 10% e agora é no valor de {(salario* 11) / 10:.2f} R$')
else:
    print(f'Seu salario teve o aumento de 15% e agora é no valor de {(salario * 115) / 100:.2f} R$')