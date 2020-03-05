'''
01. Faça um Programa que peça dois números e imprima o maior deles.
'''
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))

if n1 > n2:
    print(f'O numero {n1} é maior.')
elif n2 > n1:
    print(f'O numero {n2} é maior.')
else:
    print(f'Os numeros são iguais.')
