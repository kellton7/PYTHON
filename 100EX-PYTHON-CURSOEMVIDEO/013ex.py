#Faça um algoritmo que leia o salario  de um funcionario e mostre seu novo salario  com 15 de aumento

salario = float(input('Qual o seu salario: R$'))
aumento = salario * 15

print(f'O seu novo salario com 15% a mais é: {(aumento  / 100) + salario:.2f}')
