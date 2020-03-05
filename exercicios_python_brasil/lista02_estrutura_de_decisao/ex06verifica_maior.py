'''
06. Faça um Programa que leia três números e mostre o maior deles.
'''
num = 0
maior = 0
cont = 0
while cont <= 2:
    cont += 1
    num = float(input(f'Digite o {cont}° numero: '))
    if cont == 1:
        maior=num
    else:
        if num > maior:
            maior = num

print(f'Dos numeros digitados esse é o maior numero {maior}')