#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar.  Calcule o valor da prestação mensal, sabendo que
#ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Olá, digite o valor da casa: R$'))
salario = float(input('Digite o seu salário mensal: R$'))
anos = int(input('Deseja pagar em quantos anos: '))

prestacaoMensal = valorCasa / (anos * 12)
aprovar = (30 * salario) / 100

print(f'Para pegar uma casa de R${valorCasa:.2f} em {anos} anos o empréstimo vai ser de R${prestacaoMensal:.2f}')
if prestacaoMensal <= aprovar:
    print('Epréstimo bancário APROVADO!')
else:
    print('Empréstimo bacário NEGADO!')
