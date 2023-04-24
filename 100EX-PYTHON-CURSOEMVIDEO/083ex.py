#Crie um programa onde o usuário digite um expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada
#está com s parênteses abertos e fechados na ordem correta
expressao = []
exp = str(input('DIGITE SUA ESPRESSÂO: '))
for parent in exp:
    if parent == '(':
        expressao.append('(')
    elif parent == ')':
        if len(expressao) > 0:
            expressao.pop()
        else:
            expressao.append(')')
            break
if len(expressao) == 0:
    print('SUA EXPRESSÃO ESTÁ CORRETA!')
else:
    print('SUA EXPRESSÃO ESTÁ ERRADA!')

