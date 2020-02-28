'''
06. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''

raio= int(input('Digite o raio do circulo a ser calculado: '))

pi = 3.14159
area = pi * raio**2
print(f'Dado o raio de {raio} a area do circulo é igual a {area :.2f}')