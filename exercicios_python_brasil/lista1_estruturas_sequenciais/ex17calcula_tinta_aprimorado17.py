'''
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

print('    CALCULO PARA COMPRA DE TINTA!!!!')

alt= float(input('Digite a altura das paredes a serem pintada: \n '))

larg= float(input('Digite o comprimento total das paredes a serem pitadas:\n '))

mt2= alt*larg
cobertura = mt2/6
cobertura10 = cobertura/100*10

lata = 18
qlt = cobertura / lata
qlt = int(float(qlt))
if cobertura/lata < 1:
    qlt = 1
elif cobertura%lata != 0:
    qlt += 1

galao = 3.6
qgl = cobertura/galao
qgl = int(float(qgl))
if cobertura/galao < 1:
    qgl = 1
elif cobertura % galao != 0:
    qgl += 1

coberturacombo=cobertura + cobertura10
combo = coberturacombo % lata
combo = int(float(combo))
qltcombo=coberturacombo / lata
qltcombo = int(float(qltcombo))
qglcombo = combo / galao
qglcombo = int(float(qglcombo))
if combo / galao < 0:
    qglcombo = 1
elif combo % galao != 0:
    qglcombo += 1


print(f'Para a medida {mt2}MT²')
print(f'São necessarios {cobertura} litros de tinta')
print(f'Devera comprar {qlt } latas de tinta 18 lt totalizando {qlt*lata:.2f} litros')
print(f'Valor unitario R$80.00    TOTAL:R${qlt * 80 :.2f}\n')

print(f'Ou comprar {qgl } galões de 3.6 litros totalizando {qgl*galao :.2f} litros')
print(f'Valor unitario R$25.00    TOTAL:R${qgl * 25 :.2f}\n')

print(f'Para a medida {mt2}MT²')
print(f'São necessarios {cobertura} litros de tinta dando uma folga de 10% {coberturacombo} litros')
print(f'Devera comprar {qltcombo} latas de 18lt e {qglcombo} galões de 3.6lt totalizando {qltcombo*lata + qglcombo*galao} litro')
print(f'Valor unitario R$80.00    TOTAL:R${qltcombo * 80 :.2f}\n')
print(f'Valor unitario R$25.00    TOTAL:R${qglcombo * 25 :.2f}\n')
print(f'Total a pagar R${qltcombo*80 + qglcombo*25}')