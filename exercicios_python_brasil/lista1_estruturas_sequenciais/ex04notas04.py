'''
04. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

cont = 1
soma=0
while cont < 5:
    nota= float(input(f'Digite a {cont}° nota : '))
    cont +=1
    soma+=nota

print(f'A media entre as notas é igual {soma/4}')