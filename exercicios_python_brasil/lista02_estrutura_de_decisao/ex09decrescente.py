'''
09. Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
num1 = float(input(f'Digite o 1° numero: '))
num2 = float(input(f'Digite o 2° numero: '))
num3 = float(input(f'Digite o 3° numero: '))

list=[num1,num2,num3]
list.sort()
list.reverse()


print(f'Os numeros em ordem decrescente são {list}')