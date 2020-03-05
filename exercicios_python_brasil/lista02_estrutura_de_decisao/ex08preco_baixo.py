'''
08. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
'''
preco = 0
menor = 0
cont = 0
while cont <= 2:
    cont += 1
    preco = float(input(f'Digite o preço de {cont}° item: R$'))
    if cont == 1:
        menor=preco
    else:
        if preco < menor:
            menor = preco

print(f'Você deve comprar o item que custa R${menor}')