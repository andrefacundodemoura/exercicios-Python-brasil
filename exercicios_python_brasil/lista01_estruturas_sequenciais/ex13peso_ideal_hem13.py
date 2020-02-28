'''
13. Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

alt= float(input('Qual sua altura em mts: '))
sexo=''
while sexo != 'M' or 'F':
    sexo = str(input('Qual seu sexo [M/F] :')).strip().upper()
    if sexo == 'M':
        pesoh= (72.7*alt)-52
        print(f'Baseado na sua altura de {alt}mt seu peso ideal é {pesoh :.2f}kg')
        break
    elif sexo == 'F':
        pesom= (62.1*alt)-44.7
        print(f'Baseado na sua altura de {alt}mt seu peso ideal é {pesom :.2f}')
        break
    else:
        print('sexo invalido')

