'''
08. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

preco= float(input('Digite o valor da hora de trabalho :$ '))
horas= int(input('Digite quantas horas feitas no mes : '))

total=preco*horas

print(f'calculando {horas} horas trabalhadas sendo a hora trabalhada ${preco} temos o total a pagar de ${total}')