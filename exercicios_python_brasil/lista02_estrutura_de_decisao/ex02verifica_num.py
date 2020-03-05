'''
02. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
num = float(input('Digie um valor qualquer: '))

if num < 0:
    print(f'O numero digitado [{num}] é negativo.')
elif num == 0:
    print('0 é nulo')
else:
    print(f'O numero digitado [{num}] é positivo.')
