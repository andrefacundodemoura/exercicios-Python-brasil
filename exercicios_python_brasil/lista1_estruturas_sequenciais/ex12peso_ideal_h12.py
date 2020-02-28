'''
12. Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''

alt= float(input('Qual sua altura em mts: '))

pesoh= (72.7*alt)-52
print(f'Baseado na sua altura de {alt}mt seu peso ideal é {pesoh :.2f}kg')