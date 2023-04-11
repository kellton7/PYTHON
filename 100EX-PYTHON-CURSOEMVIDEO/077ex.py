#Crie um programa que tenha uma tupla com várias palavras, Depois disso, você de ve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Avaliaçao','Inovar','Escola','Exame','Importa','Grau','Direito','Humanismo',
            'Diretor','Faculdade')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end= ' ')