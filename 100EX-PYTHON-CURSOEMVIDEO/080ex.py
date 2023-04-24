#Programa onde o usuário possa digitar cinco valores numericos e cadastre-os em uma lista, já na possição correta de inserção
#se usar o sort(). No final mostre a lista ordenada na tela.
valores = []
for c in range(0, 5):
    n = int(input('DIGITE UM VALOR: '))
    if c == 0 or n > valores[- 1]:
        valores.append(n)
        print('Adicioando ao final da lista!')
    else:
        pos = 0 
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na {pos} da lista!')
                break
            pos += 1
print('-'*50)
print(f'OS VALORES DIGITADOS FORAM: {valores}')
