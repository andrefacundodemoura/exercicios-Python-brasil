'''
09. Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
'''

f= float(input(f'Digite os graus e °F para conversão : '))

c= 5*(f-32)/9
print(f'Tendo a temperatura de {f}°F é igual a {c :.2f}°C ')