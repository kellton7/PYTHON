#Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra A
#em qual posição ela aparece a primeira vez
#em qula posição ela aparece a ultima vez

frase = str(input('Digite uma frase qualquer: ')).strip().lower()
#d = frase.split()
print(f'Essa frase tem {frase.count("a")} letra a: ')
print(f'A primerira letra "a" aparece na posição: {frase.find("a")+ 1}')
print(f'A ultima posição que a letra "a" aparece é: {frase.rfind("a")+ 1}')





