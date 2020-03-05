'''
10. Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
hr=''
while hr != 'M' or 'V' or 'N':
    hr=str(input('Digite qual o seu horario de estudos')).upper()
    if hr in 'MVN':
        break
    else:
        print('Opção invalida')

if hr == 'M':
    print('Bom dia')
elif hr == 'V':
    print('Boa tarde')
elif hr == 'N':
    print('Boa noite')