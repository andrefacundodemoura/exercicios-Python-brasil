'''
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''

n1int= int(input('Digite um numero inteiro: '))
n2int= int(input('Digite outro numero inteiro: '))

nreal= float(input('Digite um numero real qualquer: '))

print(f'''
Com esses dados faremos os seguintes calculos:
a. O produto do dobro do primeiro com metade do segundo : {n1int*2} X {n2int/2} = {(n1int*2)*(n2int/2)}
b. A soma do triplo do primeiro com o terceiro : {n1int*3} + {nreal} = {(n1int*3)+nreal}
c. O terceiro elevado ao cubo : {nreal}³ = {nreal**3}
''')