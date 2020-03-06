'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores
podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é:
 equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''
l1 = float(input('Digite um dos lados do triangulo '))
l2 = float(input('Digite um dos lados do triangulo '))
l3 = float(input('Digite um dos lados do triangulo '))

if l1+l2 > l3 and l2+l3 > l1 and l1+l3 > l2:
    if l1 == l2 == l3:
            print('Forma um triangulo equilatero')
    elif l1 == l2 or l2 == l3 or l3 ==l1:
        print('Forma um triangulo isóceles')
    else:
        print('Forma um triangulo escaleno')
else:
    print('NÃO É POSIVEL FORMAR TRIANGULO')