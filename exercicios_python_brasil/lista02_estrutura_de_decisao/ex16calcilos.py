'''
16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa
não deve fazer pedir os demais valores, sendo encerrado;

Se o delta calculado for negativo, a equação não possui raizes reais.
Informe ao usuário e encerre o programa;

Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
print('ax² + bx + c = 0')
a=float(input('Digite o termo (a) da equação: '))
if a == 0:
    print('A equação não de segundo grau programa encerrado ')
else:
    b=float(input('Digite o termo (b) da equação: '))
    c=float(input('Digite o termo (c) da equação: '))

    delta = b**2 - 4*a*c
    xpos = 0
    xneg = 0
    result = 0

    if delta < 0:
        print(' A equação não possui raizes reais.')
    elif delta == 0:
        xpos = (-b + delta ** 0.5) / (2 * a)
        xneg = (-b - delta ** 0.5) / (2 * a)
        result = (a*xpos**2) + (b*xpos) + c
        print(f'A equação possui apenas uma raiz real ')
        print(f'A sua raiz real = {xpos}')
    elif delta > 0:
        xpos = (-b + delta ** 0.5) / (2 * a)
        xneg = (-b - delta ** 0.5) / (2 * a)
        result = (a * xneg ** 2) + (b * xneg) + c
        print('A equação possui duas raiz reais')
        print(f'x = {xpos} e x = {xneg}')



