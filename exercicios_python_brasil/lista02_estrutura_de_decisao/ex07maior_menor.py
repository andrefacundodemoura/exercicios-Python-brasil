'''
07. Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
num = 0
maior = 0
menor = 0
cont = 0
while cont <= 2:
    cont += 1
    num = float(input(f'Digite o {cont}° numero: '))
    if cont == 1:
        maior=num
        menor=num
    else:
        if num > maior:
             maior = num
        if num < menor:
            menor = num

print(f'Dos numeros digitados esse é o maior numero {maior} e esse é o menor {menor}')