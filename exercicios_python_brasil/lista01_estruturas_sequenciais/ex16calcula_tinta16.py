'''
16. Faça um programa para uma loja de tintas.
 O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
 em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

print('    CALCULO PARA COMPRA DE TINTA!!!!')

alt= float(input('Digite a altura das paredes a serem pintada: \n '))

larg= float(input('Digite o comprimento total das paredes a serem pitadas:\n '))

mt2= alt*larg
cobertura = mt2/3

lata = 18

qlt = cobertura/lata
qltconvertido = int(float(qlt))

if cobertura/lata <1 :
    qltconvertido=1

elif cobertura%lata !=0:
    qltconvertido+=1

print(f'Para a medida {mt2}MT²')
print(f'São necessarios {cobertura} litros de tinta')
print(f'Devera comprar {qltconvertido } latas de tinta')
print(f'Valor unitario R$80.00    TOTAL:R${qltconvertido * 80}')

